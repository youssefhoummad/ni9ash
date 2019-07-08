def get_object_or_none(model, *args, **kwargs):
    try:
        return model._default_manager.get(*args, **kwargs)
    except model.DoesNotExist:
        return None


def get_object_or_this(model, this, *args, **kwargs):
    return get_object_or_none(model, *args, **kwargs) or this
