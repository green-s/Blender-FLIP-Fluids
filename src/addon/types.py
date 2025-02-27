# Blender FLIP Fluid Add-on
# Copyright (C) 2019 Ryan L. Guy
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

object_types = (
    ('TYPE_NONE',     "None",     "", 0),
    ('TYPE_DOMAIN',   "Domain",   "Bounding box of this object represents the computational domain of the fluid simulation", 1),
    ('TYPE_FLUID',    "Fluid",    "Object represents a volume of fluid in the simulation", 2),
    ('TYPE_OBSTACLE', "Obstacle", "Object represents an obstacle", 3),
    ('TYPE_INFLOW',   "Inflow",   "Object adds fluid to the simulation", 4),
    ('TYPE_OUTFLOW',  "Outflow",  "Object removes fluid from the simulation", 5)
    )

frame_range_modes = (
    ('FRAME_RANGE_TIMELINE', "Timeline", "Use the start and end frame range from the timeline"),
    ('FRAME_RANGE_CUSTOM',   "Custom",   "Use a custom start and end frame range")
    )

frame_offset_types = (
    ('OFFSET_TYPE_TIMELINE', "Timeline Frame", "Trigger fluid object at frame in timeline"),
    ('OFFSET_TYPE_FRAME',    "Frame Offset",   "Trigger fluid object at a frame offset from start of the simulation")
    )

fluid_velocity_modes = (
    ('FLUID_VELOCITY_MANUAL', "Manual", "Set fluid velocity vector manually."),
    ('FLUID_VELOCITY_TARGET', "Target", "Set fluid velocity vector towards a target object.")
    )

inflow_velocity_modes = (
    ('INFLOW_VELOCITY_MANUAL', "Manual", "Set inflow velocity vector manually."),
    ('INFLOW_VELOCITY_TARGET', "Target", "Set inflow velocity vector towards a target object.")
    )

mesh_types = (
    ('MESH_TYPE_RIGID',  "Rigid",      "Mesh shape does not change/deform during animation."),
    ('MESH_TYPE_DEFORM', "Deformable", "Mesh shape changes/deforms during animation. Slower to calculate, only use if really necessary.")
    )

display_modes = (
    ('DISPLAY_NONE',    "None",    "Display nothing"),
    ('DISPLAY_PREVIEW', "Preview", "Display preview quality results"),
    ('DISPLAY_FINAL',   "Final",   "Display final quality results")
    )

whitewater_view_settings_modes = (
    ('VIEW_SETTINGS_WHITEWATER',        "Whitewater",        "Adjust view settings for all whitewater particles"),
    ('VIEW_SETTINGS_FOAM_BUBBLE_SPRAY', "Spray Bubble Foam", "Adjust view settings for foam, bubble, and spray particles separately")
    )

whitewater_object_settings_modes = (
    ('WHITEWATER_OBJECT_SETTINGS_WHITEWATER',        "Whitewater",        "Adjust particle object settings for all whitewater particles"),
    ('WHITEWATER_OBJECT_SETTINGS_FOAM_BUBBLE_SPRAY', "Spray Bubble Foam", "Adjust particle object settings for foam, bubble, and spray particles separately")
    )

whitewater_ui_modes = (
    ('WHITEWATER_UI_MODE_BASIC',    "Basic",    "Display only the basic and most important whitewater simulation parameters"),
    ('WHITEWATER_UI_MODE_ADVANCED', "Advanced", "Display all whitewater simulation parameters")
    )

cache_info_modes = (
    ('CACHE_INFO', "Cache Info", "Display info about the entire simulation cache"),
    ('FRAME_INFO', "Frame Info", "Display info about a single simulation frame")
    )

csv_regions = (
    ('CSV_REGION_US',  "US",  "US format - Decimals in numbers (1.23), commas to separate values"),
    ('CSV_REGION_EUR', "EUR", "European format - Commas in numbers (1,23); semicolons to separate values")
    )

boundary_behaviours = (
    ('BEHAVIOUR_KILL',      "Kill",      "Kill any foam particles when outside boundary limits"),
    ('BEHAVIOUR_BALLISTIC', "Ballistic", "Make foam particles follow ballistic trajectory"),
    ('BEHAVIOUR_COLLIDE',   "Collide",   "Collide with boundary limits")
    )

gravity_types = (
    ('GRAVITY_TYPE_CUSTOM', "Custom", "Use custom gravity values"),
    ('GRAVITY_TYPE_SCENE',  "Scene",  "Use scene gravity values")
    )

surface_compute_chunk_modes = (
    ('COMPUTE_CHUNK_MODE_AUTO',  "Auto",  "Automatically determine the number of compute chunks, based on meshing grid dimensions"),
    ('COMPUTE_CHUNK_MODE_FIXED', "Fixed", "Manually determine the number of compute chunks")
    )

meshing_volume_modes = (
    ('MESHING_VOLUME_MODE_DOMAIN',  "Domain Volume", "Mesh all fluid that is inside of the domain."),
    ('MESHING_VOLUME_MODE_OBJECT',  "Object Volume", "Mesh only fluid that is inside of a custom object.")
    )

obstacle_meshing_modes = (
    ('MESHING_MODE_INSIDE_SURFACE',  "Inside Surface",  "Generate fluid-solid interface on the inside of the obstacle. Fluid surface will penetrate the obstacle."),
    ('MESHING_MODE_ON_SURFACE',      "On Surface",      "Generate fluid-solid interface directly on the obstacle surface. May lead to rendering artifacts."),
    ('MESHING_MODE_OUTSIDE_SURFACE', "Outside Surface", "Generate fluid-solid interface on the outside of the obstacle. Leaves a gap between the fluid surface and obstacle.")
    )

threading_modes = (
    ('THREADING_MODE_AUTO_DETECT', "Auto-detect", "Automatically determine the number of threads, based on CPUs"),
    ('THREADING_MODE_FIXED',       "Fixed",       "Manually determine the number of threads")
    )

grid_display_modes = (
    ('GRID_DISPLAY_SIMULATION', "Simulation Grid",   "Display the domain simulation grid"),
    ('GRID_DISPLAY_MESH',       "Final Mesh Grid",   "Display the domain surface mesh grid"),
    ('GRID_DISPLAY_PREVIEW',    "Preview Mesh Grid", "Display the domain surface preview mesh grid"),
    )

gradient_interpolation_modes = (
    ('GRADIENT_NONE', "No Gradient",  "Do not interpolate between colors"),
    ('GRADIENT_RGB',  "RGB Gradient", "Interpolate between colors in RGB colorspace"),
    ('GRADIENT_HSV',  "HSV Gradient", "Interpolate between colors in HSV colorspace"),
    )

material_types = (
    ('MATERIAL_TYPE_SURFACE',    "Surface",    "Material suitable for surface mesh"),
    ('MATERIAL_TYPE_WHITEWATER', "Whitewater", "Material suitable for whitewater mesh"),
    ('MATERIAL_TYPE_ALL',        "All",        "Material suitable for any mesh"),
    )
