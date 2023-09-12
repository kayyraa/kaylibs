def notify(title, message, duration, icon, path):
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    if icon:
        toaster.show_toast(str(title), str(message), duration=duration, icon_path=path)
    else:
        toaster.show_toast(str(title), str(message), duration=duration)