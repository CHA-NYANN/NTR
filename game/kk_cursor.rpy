# User-made cursor assets. UI-only: clicks still reach the screen underneath.
init 80 python:
    import time as _kk_cursor_time
    import pygame_sdl2 as _kk_cursor_pygame

    KK_CURSOR_HOTSPOT = (57, 17)
    KK_CURSOR_FRAME_SECONDS = .140

    class KouseikanCursor(renpy.Displayable):
        def __init__(self):
            super(KouseikanCursor, self).__init__()
            self.idle = renpy.displayable("kursor/diam.png")
            self.frames = [renpy.displayable("kursor/klik_%02d.png" % i) for i in range(1, 7)]
            self.clicked_at = None

        def frame_index(self, now):
            if self.clicked_at is None:
                return None
            elapsed = now - self.clicked_at
            if elapsed < 0 or elapsed >= len(self.frames) * KK_CURSOR_FRAME_SECONDS:
                return None
            return int(elapsed / KK_CURSOR_FRAME_SECONDS)

        def render(self, width, height, st, at):
            result = renpy.Render(width, height)
            x, y = renpy.get_mouse_pos()
            if not renpy.is_mouse_visible() or not (0 <= x < width and 0 <= y < height):
                return result
            now = _kk_cursor_time.monotonic()
            index = self.frame_index(now)
            picture = self.idle if index is None else self.frames[index]
            cursor = renpy.render(picture, 128, 128, st, at)
            result.blit(cursor, (x - KK_CURSOR_HOTSPOT[0], y - KK_CURSOR_HOTSPOT[1]))
            if index is not None:
                elapsed = now - self.clicked_at
                renpy.redraw(self, max(.001, KK_CURSOR_FRAME_SECONDS - elapsed % KK_CURSOR_FRAME_SECONDS))
            else:
                # Keep Ren'Py's normal inactivity/controller visibility behavior.
                renpy.redraw(self, 1.0)
            return result

        def event(self, ev, x, y, st):
            if ev.type == _kk_cursor_pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.clicked_at = _kk_cursor_time.monotonic()
                renpy.redraw(self, 0)
            # Returning None leaves buttons, dialogue advance and dragging intact.
            return None

        def visit(self):
            return [self.idle] + self.frames

    _kk_cursor = KouseikanCursor()

    def kk_cursor_displayable():
        if renpy.variant("touch") or _preferences.system_cursor:
            return None
        return _kk_cursor

    config.mouse_displayable = kk_cursor_displayable
