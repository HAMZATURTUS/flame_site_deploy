from wagtailcache.cache import clear_cache
from wagtail import hooks

@hooks.register('after_create_page')
@hooks.register('after_edit_page')
def clear_wagtailcache(request, page):
    if page.live:
        clear_cache()  # Clears the Wagtail cache for the entire site