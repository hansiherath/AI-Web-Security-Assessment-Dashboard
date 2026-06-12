try:
    import importlib
    st = importlib.import_module("streamlit")
    cache_data = st.cache_data
except Exception:
    st = None
    def cache_data(func):
        return func


@cache_data
def detect_technology(url):
    try:
        import importlib
        builtwith = importlib.import_module("builtwith")
    except Exception as e:
        return {"Error": ["builtwith import failed: %s" % str(e), "Install the 'builtwith' package."]}

    try:
        tech = builtwith.parse(url)
        if not tech:
            return {"Info": ["No technologies detected"]}
        return tech
    except Exception as e:
        return {"Error": [str(e)]}