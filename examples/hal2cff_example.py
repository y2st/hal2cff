from hal2cff import hal2cff

# # hal2cff example


print(hal2cff("https://hal.archives-ouvertes.fr/hal-01361430v1"))

import ipywidgets as widgets

query = widgets.Textarea(value="https://hal.archives-ouvertes.fr/hal-01361430v1")
button = widgets.Button(description="Run query")
display(widgets.HBox([query, button]))
output = widgets.Output()
display(output)


def run_and_display_query(_):
    hal2cff(query.value)
    with output:
        display(hal2cff(query.value))


button.on_click(run_and_display_query)
