class BaseView:

    current_view = None

    @staticmethod
    def get_view(view):
        BaseView.current_view = view
        return view()

    @staticmethod
    def rerender(*args, **kwargs):
        if args and callable(args[0]):
            func = args[0]
            return BaseView.render_wrapper()(func)
        update_key = kwargs.get('update')
        return BaseView.render_wrapper(update_key=update_key)

    @staticmethod
    def render_wrapper(update_key=None):
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                view = BaseView.current_view()
                if update_key:
                    state = view.state
                    state['data'][update_key] = result
                    view.state = state
                    view.render()
                    return result
                view.render()
                return result
            return wrapper
        return decorator
