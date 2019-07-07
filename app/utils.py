def get_object_or_none(model, *args, **kwargs):
    try:
        return model._default_manager.get(*args, **kwargs)
    except model.DoesNotExist:
        return None
