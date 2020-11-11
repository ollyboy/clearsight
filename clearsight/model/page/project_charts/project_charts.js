frappe.pages['project-charts'].on_page_load = function(wrapper) {

   var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Project Charts',
		single_column: true
	});
    
    // hidden div 
    wrapper = $(wrapper).find('.layout-main-section');
    wrapper.append(`<div id="my_chart"></div>`);


//new SlimSelect({
//  select: '#slim-select'
//})


    // define empty arrays for chart call
    var y_axis = [];
    var plan_capex = [];
    var actual_capex = [];
    var plan_fte = [];
    var actual_fte = [];
  
    // read a data set from a summary doc
    frappe.call({
      method:"frappe.client.get_list",
      args: {
        doctype:"Finance Resource forcast",
	    filters: [ ],
        fields:["csfr_week_end", "csfr_plan_capex", "csfr_actual_capex", "csfr_plan_fte" , "csfr_actual_fte"  ]
            }, 
        
      callback: function(data) {

	    // build arrays suitable to pass to charts
            for (let key in data) { 
              	let value = data[key]; 
              	for (i = 0; i < value.length; i++) { 
              		plan_capex.push(value[i].csfr_plan_capex || 0 ); 
              		actual_capex.push(value[i].csfr_actual_capex || 0 ); 
              		plan_fte.push(value[i].csfr_plan_fte || 0); 
              		actual_fte.push(value[i].csfr_actual_fte || 0 ); 
              		y_axis.push(value[i].csfr_week_end || 0 );
              		//console.log ( value[i].csfr_week_end );
              	} 
              }
       }
    });

    let chart = new frappe.Chart( "#my_chart", { // or DOM element
	data: {
	
		labels: y_axis,

	datasets: [
		{
			name: "Plan Capex", chartType: 'bar',
			values: plan_capex
		},
		{
			name: "Actual Capex", chartType: 'bar',
			values: actual_capex
		},
		{
			name: "Plan FTEs", chartType: 'line',
			values: plan_fte
		},
		{
			name: "Actual FTEs", chartType: 'line',
			values: actual_fte
		}
	],

	//yMarkers: [{ label: "Marker", value: 70,
	//	options: { labelPos: 'left' }}],
	//yRegions: [{ label: "Region", start: -10, end: 50,
	//	options: { labelPos: 'right' }}]
	},

	title: "Finance Resource forcast",
	type: 'axis-mixed', // or 'bar', 'line', 'pie', 'percentage'
	height: 300,
	colors: ['purple', '#ffa3ef', 'light-blue', 'green'],

	tooltipOptions: {
		formatTooltipX: d => (d + '').toUpperCase(),
		formatTooltipY: d => d + ' pts',
	}
  });

  // hacks to make the hidden div visible
  setTimeout(function(){ window.dispatchEvent(new Event('resize')); }, 100);
  
}
