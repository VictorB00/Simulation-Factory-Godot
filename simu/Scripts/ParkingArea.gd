extends Area2D

var parking_area_name : String
var cells : Array #contains the cells of the parking_area
func _ready():
	ExportManager.add_export_static(self)
	
	#generate a name 
	parking_area_name = ExportManager.new_name("parking_area")
	
func get_name() -> String:
	return parking_area_name

func _on_ParkingArea_body_entered(body):
	if body.is_in_group("robots"):
		body.set_in_station(true)

func _on_ParkingArea_body_exited(body):
	if body.is_in_group("robots"):
		body.set_in_station(false)

func export_static() -> Array:
	var export_data = []
	export_data.append(["parking_area", parking_area_name])
	export_data.append(["cells", parking_area_name, cells])
	
	if get_children().size()>0:
		var collision_polygon = get_child(0)
		export_data.append(["polygon", parking_area_name, ExportManager.convert_array_pixels_to_meters(collision_polygon.get_polygon())])

	return export_data
