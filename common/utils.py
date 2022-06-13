def create_message (error,message, data,status=None):
    if not status:
        if error:
            status = 500
        else:
            status = 200

    return {"status": status, "error": error, "message": message, "data": data}
