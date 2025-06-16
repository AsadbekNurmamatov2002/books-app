from unfold.admin import DashboardCallback

def dashboard_callback(request, context):
    context.update(
        {
            "sample": "dashboard",
        }
    )
    return context