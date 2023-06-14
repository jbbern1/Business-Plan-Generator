from django.shortcuts import render
from django.http import HttpResponse
from myapp import gpt_interface


def text_input(request):
	# if submit is pressed
	if request.method == 'POST':
		# Handle form submission
		elevator_pitch = request.POST['elevator_pitch']
		extras_titles = ["product_service_description",
				   "revenue_model",
				   "target_market",
				   "marketing_channels",
				   "competitive_analysis",
				   "pricing_strategy",
				   "sales_strategy",
				   "operational_plan",
				   "financial_projections",
				   "funding_needs",
				   "risk_analysis",
				   "exit_strategy"]
		extras = [request.POST[name] for name in extras_titles]

		# Perform necessary processing on the inputs
		processed_output = gpt_interface.web_callable(elevator_pitch, extras, verbose=True) 
		# processed_output = gpt_interface.call_gpt_4(elevator_pitch, verbose=True) 

		# Pass the processed output to the template
		context = {'output': processed_output}
		return render(request, 'output.html', context)

	# Render the initial form if the request method is GET
	return render(request, 'input.html')

# Command to run website:
# python manage.py runserver