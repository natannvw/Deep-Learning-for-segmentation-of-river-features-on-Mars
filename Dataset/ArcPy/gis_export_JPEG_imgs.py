import os

aprx            = arcpy.mp.ArcGISProject("CURRENT")
layer           = 'Giulia Valleys'

dir_name        = r'C:\Users\natan\Google Drive\Weizmann\first_year\Courses\second_semester\Deep_learning\Project\GIS'     # destination dir

layout          = aprx.listLayouts("*")[1]
map_frame       = layout.listElements('MAPFRAME_ELEMENT', "*")[0]

num_segments    = arcpy.management.GetCount(valleys)
num_segments    = int(num_segments[0])

for i in range(num_segments):

    # Select segment:
    arcpy.management.SelectLayerByAttribute(layer, "NEW_SELECTION", f"FID = {str(i)}")

    # Zoom (in map frame) & Clear selection:
    map_frame.zoomToAllLayers(selection_only = True)
    arcpy.SelectLayerByAttribute_management(layer, "CLEAR_SELECTION", f"FID = {str(i)}")

    # Export layout:
    base_filename   = f'FID_{str(i)}.jpg'
    new_path        = os.path.join(dir_name, base_filename)

    layout.exportToJPEG(new_path, 50, '24-BIT_TRUE_COLOR', 100, 'False', 'False')


