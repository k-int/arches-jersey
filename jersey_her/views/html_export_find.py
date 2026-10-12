from django.shortcuts import render
from arches.app.utils.data_management.resources.formats.htmlfile import HtmlWriter


def html_export_find(request):

    html_writer = HtmlWriter()

    # resource_instance_id = "ea45e9ee-50e0-418d-b13a-0c3909239287"
    resource_instance_id = "cd45efbc-d9b7-4617-9f18-7f54dbfee5c4"

    resource_list = html_writer.fetch_resource_objects_list(
        resourceinstanceids=[resource_instance_id],
        allowed_graph_ids=["3af584c3-fd4d-11e6-9e3e-026d961c88e6"],
    )

    resource = resource_list["3af584c3-fd4d-11e6-9e3e-026d961c88e6"][0]

    return render(
        request,
        "html_export/3af584c3-fd4d-11e6-9e3e-026d961c88e6.htm",
        {"resources": [resource]},
    )
