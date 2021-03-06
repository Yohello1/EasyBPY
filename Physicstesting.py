#Setting the type of fluid (domain,flow,effector, or none)
#booleans can only be a int or a bool, not a string
# 1 = on, 0 = off
#Fluid > domain > Viewport > Grid > On hold 


def set_fluid_type_none():
    bpy.context.object.modifiers["Fluid"].fluid_type = 'NONE'

def set_fluid_type_domain():
    bpy.context.object.modifiers["Fluid"].fluid_type = 'DOMAIN'

def set_fluid_type_flow():
    bpy.context.object.modifiers["Fluid"].fluid_type = 'FLOW'

def set_fluid_type_effector():
    bpy.context.object.modifiers["Fluid"].fluid_type = 'EFFECTOR'


#Effector parameters 

#Effector Type
def fluid_effector_type(type):
    bpy.context.object.modifiers["Fluid"].effector_settings.effector_type = type
      
#Sampling Substeps
def fluid_effector_subsample_value(value):
    intvalue = int(value)
    bpy.context.object.modifiers["Fluid"].effector_settings.subframes = intvalue

#surface thickness
def fluid_effector_thickness_value(value):
    intvalue = int(value)
    bpy.context.object.modifiers["Fluid"].effector_settings.surface_distance = intvalue

#Use effector, 1 = on 0 = off
def fluid_effector_use(fbool):
    bool = int(fbool)
    bpy.context.object.modifiers["Fluid"].effector_settings.use_effector = bool
    
#Is Planar, 1 = on 0 = off
def fluid_effector_isplanar(fbool):
    bool = int(fbool)
    bpy.context.object.modifiers["Fluid"].effector_settings.use_plane_init = bool

#enabling velocity
def fluid_effector_velocity(value):
    intvalue = int(value)
    bpy.context.object.modifiers["Fluid"].effector_settings.velocity_factor = intvalue

#Guide Mode 
def fluid_effector_guide_mode(value):
    if value == 'MAXIMUM' or value == 'MAX':
        bpy.context.object.modifiers["Fluid"].effector_settings.guide_mode = 'MAXIMUM'
    if value == 'MINIMUM' or value == 'MIN':
        bpy.context.object.modifiers["Fluid"].effector_settings.guide_mode = 'MINIMUM'
    if value == 'OVERRIDE' or value == 'OVER':
        bpy.context.object.modifiers["Fluid"].effector_settings.guide_mode = 'OVERRIDE'
    if value == 'AVERAGED' or value == 'MEAN':
        bpy.context.object.modifiers["Fluid"].effector_settings.guide_mode = 'AVERAGED'
            
#Type Flow parameters

#setting the 'flow type'
def flow_type_set_smoke():
    bpy.context.object.modifiers["Fluid"].flow_settings.flow_type = 'SMOKE'

def flow_type_set_fire():
    bpy.context.object.modifiers["Fluid"].flow_settings.flow_type = 'FIRE'
    
def flow_type_set_fire_smoke():
    bpy.context.object.modifiers["Fluid"].flow_settings.flow_type = 'BOTH'
    
def flow_type_set_fluid():
    bpy.context.object.modifiers["Fluid"].flow_settings.flow_type = 'LIQUID'
    
#flow behavior
def flow_set_behavoir(value):
    bpy.context.object.modifiers["Fluid"].flow_settings.flow_behavior = value

#Use flow
def flow_use_flow(value):
    bool = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.use_inflow = bool

#flow source, liquids
def flow_source(value):
    if value == 'PARTICLE SYSTEM':
        value = 'PARTICLES'
    bpy.context.object.modifiers["Fluid"].flow_settings.flow_source = value

#smoke colour
def flow_smoke_colour_rgb(r,g,b):
    print(r+g+b)
    rfloat = float(r)
    gfloat = float(g)
    bfloat = float(b)
    bpy.context.object.modifiers["Fluid"].flow_settings.smoke_color = (rfloat,gfloat,bfloat)
    
#Absloute density????? what ever it is??
def flow_absolute_density(value):
    bool = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.use_absolute = bool

#Initial temprature
def flow_initial_temp(value):
    temp = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.temperature = temp
    
#Density,
def flow_density(value):
    density = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.density = density

#if they want to emit from a vertex group
def flow_vertexgroup(value):
    bpy.context.object.modifiers["Fluid"].flow_settings.density_vertex_group = value


#Particle system
#setting the particle system
def flow_particle_system_select(value):
    bpy.context.object.modifiers["Fluid"].flow_settings.particle_system = bpy.data.objects["Cube"].particle_systems[value]

def flow_particle_set_size_toggle(value):
    bool = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.use_particle_size = bool


#set size thing in particles
def flow_set_particle_size(value):
    size = float(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.particle_size = size


    
#intial Velocity
#toggle
def flow_initial_velocity_toggle(value):
    bool = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.use_initial_velocity = bool

#How much
def flow_initial_velocity_value(value):
    velocity = float(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.velocity_factor = velocity

#Domains
def fluid_domain_set_gas():
    bpy.context.object.modifiers["Fluid"].domain_settings.domain_type = 'GAS'

def fluid_domain_set_liquid():
    bpy.context.object.modifiers["Fluid"].domain_settings.domain_type = 'LIQUID'

#Global Fluid Settings
#Resolution
def fluid_domain_set_resolution(value):
    res = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.resolution_max = res
    
#Time scale
def fluid_domain_time_scale(value):
    timespeed = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.time_scale = timespeed

#CFL number (Don't know what this is )
def fluid_domain_set_cfl(value):
    CFL = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.cfl_condition = CFL

#time steps
def fluid_domain_set_timesteps_max(value):
    timestep = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.timesteps_max = timestep
    
def fluid_domain_set_timesteps_min(value):
    timestep = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.timesteps_min = timestep

#Scene gravity (Not sure if I'll add it)


#Border collisions

def fluid_domain_border_colisions(side,toggle):
    bool = int(toggle)
    if side == 'top' or side == 'TOP':
        bpy.context.object.modifiers["Fluid"].domain_settings.use_collision_border_top = bool
    if side == 'back' or side == 'BACK':
        bpy.context.object.modifiers["Fluid"].domain_settings.use_collision_border_back = bool
    if side == 'front' or side == 'FRONT':
        bpy.context.object.modifiers["Fluid"].domain_settings.use_collision_border_front = bool
    if side == 'right' or side == 'RIGHT':
        bpy.context.object.modifiers["Fluid"].domain_settings.use_collision_border_right = bool
    if side == 'left' or side == 'LEFT':
        bpy.context.object.modifiers["Fluid"].domain_settings.use_collision_border_left = bool
    if side == 'bottom' or side == 'BOTTOM':
        bpy.context.object.modifiers["Fluid"].domain_settings.use_collision_border_bottom = bool

#caches      
def fluid_domain_cache_folder(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.cache_directory = value

def fluid_simulation_start(value):
    start = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.cache_frame_start = start

def fluid_simulation_end(value):
    end = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.cache_frame_end = end

def fluid_simulation_offset(value):
    end = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.cache_frame_offset = end
    
def fluid_cache_type(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.cache_type = value
    #use REPLAY, MODULAR, and ALL

def fluid_cache_continue_toggle(value):
    bool = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.cache_resumable = bool
    
def fluid_cache_format(value):
    if value.lower() == 'openvdb':
        bpy.context.object.modifiers["Fluid"].domain_settings.cache_data_format = 'OPENVDB'
    if value.lower() == 'uni cache':
        bpy.context.object.modifiers["Fluid"].domain_settings.cache_data_format = 'UNI'
          
def fluid_cache_format(value):
    if value.lower() == 'zip':
        bpy.context.object.modifiers["Fluid"].domain_settings.openvdb_cache_compress_type = 'ZIP'
    if value.lower() == 'blosc':
        bpy.context.object.modifiers["Fluid"].domain_settings.openvdb_cache_compress_type = 'BLOSC'
    if value.lower() == 'none':
        bpy.context.object.modifiers["Fluid"].domain_settings.openvdb_cache_compress_type = 'NONE'
      
def fluid_cache_precision_vol(value):
    print(value)
    if value.lower() == 'half':
        value = "16"
    if value.lower() == 'full':
        value = "32"
    bpy.context.object.modifiers["Fluid"].domain_settings.openvdb_data_depth = value

#Collections 

def fluid_flow_collection(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.fluid_group = bpy.data.collections[value]

def fluid_flow_effectorn(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_group = bpy.data.collections[value]

#Guides

def fluid_domain_guides_toggle(value):
    bool = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_guide = bool

def fluid_domain_guide_weight(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.guide_alpha = val

def fluid_domain_guides_size(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.guide_beta = val

def fluid_domain_guides_velocity(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.guide_vel_factor = val

def fluid_domain_guides_source(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.guide_source = value.upper()

#Need to check over this command
# def fluid_domain_guides_source(value):
#     bpy.context.object.modifiers["Fluid"].domain_settings.guide_parent = bpy.data.objects[value]

#field weights
def fluid_field_weights_collection(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.collection = bpy.data.collections[value]

def fluid_field_weights_gravity(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.gravity = val

def fluid_field_weights_all(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.all = val

#The force awakens, to me being an idiot
def fluid_field_weights_force(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.force = val

#I wanted to go on this ride
def fluid_field_weights_vortex(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.vortex = val

def fluid_field_weights_magnetic(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.magnetic = val
    
def fluid_field_weights_harmonic(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.harmonic = val
    
def fluid_field_weights_charge(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.charge = val
    
def fluid_field_weights_lennardjones(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.lennardjones = val
    
def fluid_field_weights_wind(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.wind = val

def fluid_field_weights_curve_guide(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.curve_guide = val
    
def fluid_field_weights_texture(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.texture = val
    
def fluid_field_weights_smoke_flow(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.smokeflow = val

def fluid_field_weights_turbulence(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.turbulence = val

def fluid_field_weights_drag(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.drag = val

def fluid_field_weights_boid(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.boid = val
#Viewport display

def fluid_view_thickness(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.display_thickness = val

def fluid_view_interpolation(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.display_interpolation = value.upper()

def fluid_view_slices_voxel(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.slice_per_voxel = val

def fluid_view_slice_toggle(value):
    boolean = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_slice = boolean
    
def fluid_view_slice_axis(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.slice_axis = value.upper

def fluid_view_slice_position(value):
    boolean = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.slice_depth = boolean 


#I have many regrets, I don't want to do this, please help me with this
#I wish I didn't attempt this
# C.active_object.modifiers[0].domain_settings.color_ramp.elements[0].position=.5


def fluid_view_grid_toggle(value):
    boolean = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_color_ramp = boolean
    
def fluid_view_grid_scale(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.color_ramp_field_scale = val

def fluid_view_grid_color_position(pos,stop):
    val = float(pos)
    position = int(stop)
    C.active_object.modifiers["Fluid"].domain_settings.color_ramp.elements[position].position= val

def fluid_view_grid_color_hue_interpolation(value):
    bpy.context.active_object.modifiers["Fluid"].domain_settings.color_ramp.hue_interpolation = value.upper()
    
def fluid_view_grid_color(stop,encoding,r,g,b,al):
    bpy.context.active_object.modifiers["Fluid"].domain_settings.color_ramp.color_mode = encoding.upper()
    stopint = int(stop)
    red = float(r)
    green = float(b)
    blue = float(g)
    alpha = float(al)
    bpy.context.active_object.modifiers["Fluid"].domain_settings.color_ramp.elements[stopint].color = (red,green,blue,alpha)

def fluid_view_grid_stops_new(value):
    val = float(value)
    bpy.context.active_object.modifiers["Fluid"].domain_settings.color_ramp.elements.new(val)

#Send help
def fluid_view_grid_stops_remove(value):
    val = int(value)
    bpy.context.active_object.modifiers["Fluid"].domain_settings.color_ramp.elements.remove( bpy.context.active_object.modifiers["Fluid"].domain_settings.color_ramp.elements[val] )

def fluid_view_vector_dis_toggle(value):
    boolean = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_slice = boolean

def fluid_view_vector_display_type(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.vector_display_type = value.upper()
    
def fluid_view_vector_magnitude(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.vector_scale_with_magnitude = val

#Force,fluid_velocity,guide_velocity
def fluid_view_vector_field(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.vector_field = value.upper()

def fluid_view_vector_scale(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.vector_scale = val

#Gas Domain.
#Not catorogrized
def fluid_gas_buoyancy_density(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.alpha = val

def fluid_gas_buoyancy_heat(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.beta = val

def fluid_gas_buoyancy_vorticity(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.vorticity = 2

#Dissolve

def fluid_gas_dissolve_toggle(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_dissolve_smoke = val

def fluid_gas_dissolve_time(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.dissolve_speed = val
    
def fluid_gas_dissolve_slow_toggle(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_dissolve_smoke_log = val 
    
#Noise
def fluid_gas_noise_toggle(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_noise = val

def fluid_gas_noise_toggle(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.noise_scale = 2

def fluid_gas_noise_upres_factor(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.noise_scale = val
    
def fluid_gas_noise_method(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.noise_type = value.upper()

def fluid_gas_noise_strength(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.noise_strength = val

def fluid_gas_noise_scale(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.noise_pos_scale = val

def fluid_gas_noise_time(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.noise_time_anim = val

#Fire
def fluid_gas_fire_reaction_speed(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.burning_rate = val

def fluid_gas_fire_smoke(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.flame_smoke = val

def fluid_gas_fire_vorticity(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.flame_vorticity = val

def fluid_gas_fire_temp_max(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.flame_max_temp = 1

def fluid_gas_fire_temp_min(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.flame_ignition = val

def fluid_gas_fire_color_rgb(red,green,blue):
    r = float(red)
    g = float(green)
    b = float(blue)
    bpy.context.object.modifiers["Fluid"].domain_settings.flame_smoke_color = (r, g, b)


#fluid

def fluid_fluid_toggle(value):
    h = bool(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_flip_particles = h

def fluid_fluid_flip_ratio(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.flip_ratio = val

def fluid_fluid_particle_max(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sys_particle_maximum = val

def fluid_fluid_particle_radius(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.particle_radius = val

def fluid_fluid_particle_sampling(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.particle_number = val

def fluid_fluid_particle_random(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.particle_randomness = val

def fluid_fluid_cell_max(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.particle_max = val

def fluid_fluid_cell_min(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.particle_min = val

def fluid_fluid_narrow_bandwidth(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.particle_band_width = val

def fluid_fluid_frac_obs_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_fractions = h

def fluid_fluid_obs_distance(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.fractions_distance = val

def fluid_fluid_obs_threshold(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.fractions_threshold = val

def fluid_fluid_diffusion_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_diffusion = h

def fluid_fluid_diffusion_base(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.viscosity_base = val

def fluid_fluid_diffusion_exponent(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.viscosity_exponent = val

def fluid_fluid_diffusion_surface(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.surface_tension = 0

def fluid_fluid_particles_bubbles_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_bubble_particles = h

def fluid_fluid_particles_foam_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_foam_particles = h

def fluid_fluid_particles_spray_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_spray_particles = h

def fluid_fluid_particles_combined_export(value):
    value = value.replace(" ", "_")
    value = value.upper()
    print(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_combined_export = value

#
#
#   Upres is scarry
#
#

def fluid_fluid_particles_wave_crest_potential_maximum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_max_wavecrest = val

def fluid_fluid_particles_wave_crest_potential_minimum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_min_wavecrest = val

def fluid_fluid_particles_traped_air_potential_minimum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_max_trappedair = val

def fluid_fluid_particles_traped_air_potential_minimum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_min_trappedair = val

def fluid_fluid_particles_kinetic_potential_minimum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_max_energy = val

def fluid_fluid_particles_kinetic_potential_minimum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_min_energy = val

def fluid_fluid_particles_potential_radius(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_min_energy = val
    
def fluid_fluid_particles_particle_update_radius(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_min_energy = val
    
def fluid_fluid_particles_wave_crest_particle_sampling(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_sampling_trappedair = val
    
def fluid_fluid_particles_traped_air_particle_sampling(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_sampling_wavecrest = val

def fluid_fluid_particles_particle_life_maximum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_life_max = val

def fluid_fluid_particles_particle_life_minimum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_life_min = val

def fluid_fluid_particles_bubble_buoyancy(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_bubble_buoyancy = 1

def fluid_fluid_particles_bubble_drag(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_bubble_drag = 1

def fluid_fluid_particles_particles_in_boundary(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_boundary = value.upper()


#adpative domain
def fluid_domain_adapt_toggle(value):
    bool = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_adaptive_domain = bool
    
def fluid_domain_adapt_res(value):
    intval = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.additional_res = intval

def fluid_domain_adapt_margin(value):
    intval = int(value)
    if intval > 24:
        print("Too high")
    else:
        bpy.context.object.modifiers["Fluid"].domain_settings.adapt_margin = intval

def fluid_domain_adapt_threshold(value):
    floatval = float(value)
    if floatval > 1:
        print("Too high")
    else:
        bpy.context.object.modifiers["Fluid"].domain_settings.adapt_threshold = floatval
        
#colision

def collision_use(value):
    if value.upper() == "TRUE":
        bpy.context.object.collision.use = True
    else:
        bpy.context.object.collision.use = False

def collision_set_feild_absorption(value):
    val = float(value)
    bpy.context.object.collision.absorption = val

def collision_particle_pemability(value):
    val = float(value)
    bpy.context.object.collision.permeability = val

def collision_particle_sticky(value):
    val = float(value)
    bpy.context.object.collision.stickiness = val

def collision_particle_kill_toggle(value):
    if value.upper() == "TRUE":
        bpy.context.object.collision.use_particle_kill = True
    else:
        bpy.context.object.collision.use_particle_kill = False

def collision_particle_friction(value):
    val = float(value)
    bpy.context.object.collision.friction_factor = val

def collision_particle_randomize(value):
    val = float(value)
    bpy.context.object.collision.friction_random = value

def collision_particle_damping(value):
    val = float(value)
    bpy.context.object.collision.damping_factor = val

def collision_particle_randomize2(value):
    val = float(value)
    bpy.context.object.collision.damping_random = val

def collision_soft_cloth_damping(value):
    val = float(value)
    bpy.context.object.collision.damping = val

def collision_soft_cloth_friction(value):
    val = float(value)
    bpy.context.object.collision.cloth_friction = val

def collision_soft_cloth_thick_out(value):
    val = float(value)
    bpy.context.object.collision.thickness_outer = val

def collision_soft_cloth_thick_in(value):
    val = float(value)
    bpy.context.object.collision.thickness_inner = val

def collision_soft_cloth_single_side_toggle(value):
    if value.upper() == "TRUE":
        bpy.context.object.collision.use_culling = True
    else:
        bpy.context.object.collision.use_culling = False
    
def collision_soft_cloth_override_normals_toggle(value):
    if value.upper() == "TRUE":
        bpy.context.object.collision.use_normal = True
    else:
        bpy.context.object.collision.use_normal = False

#Please let this one thing stay
def deja_vu():
    print("DEJA VU")
    print("I've just been in this line before")
    print("Higher and Higher I know it's my place to gooooo")
    print("Calling you, the val is a mystery")
    print("I've wirtten these same lines a thousand times before, just slightly differently which is why I put this here. It gives me a deja vu like feeling")
        

# Rigid body
# Rigid body

def add_rigid_body():
    bpy.ops.rigidbody.object_add()

def rigidbody_type_set(value):
    bpy.context.object.rigid_body.type = value.upper()

def rigidbody_setting_animated(value):
    if value.upper() == 'FALSE':
        h = False
    elif value.upper() == 'TRUE':
        h = True
        print("Hello there")
    bpy.context.object.rigid_body.kinematic = h

def rigidbody_shape(value):
    val = value.replace(" ", "_")
    bpy.context.object.rigid_body.collision_shape = val.upper()

def rigidbody_shape_source(value):
    bpy.context.object.rigid_body.mesh_source = value.upper()

def rigidbody_surface_response_friction(value):
    val = float(value)
    bpy.context.object.rigid_body.friction = val

def rigidbody_surface_response_friction(value):
    val = float(value)
    bpy.context.object.rigid_body.restitution = val

def rigidbody_sensitivity_margin_toggle(value):
    if value.upper() == 'FALSE':
        h = False
    elif value.upper() == 'TRUE':
        h = True
    bpy.context.object.rigid_body.use_margin = h

def rigidbody_sensitivity_margin_amount("value"):
    val = float(value)
    bpy.context.object.rigid_body.collision_margin = val

def rigidbody_collection_select(value):
    val = int(value)
    bpy.context.object.rigid_body.collision_collections[val] = True

def rigidbody_collection_deselect(value):
    val = int(value)
    bpy.context.object.rigid_body.collision_collections[val] = False

def rigidbody_dynamics_damping_translation(value):
    val = float(value)
    bpy.context.object.rigid_body.linear_damping = 1


def rigidbody_dynamics_rotation(value):
    val = float(value)
    bpy.context.object.rigid_body.rotation_damping = 1

def rigidbody_dynamics_deactivation(value):
    if value.upper() == 'FALSE':
        h = False
    elif value.upper() == 'TRUE':
        h = True
    bpy.context.object.rigid_body.use_deactivation = h

def rigidbody_dynamics_deactivation_start(value)
    if value.upper() == 'FALSE':
        h = False
    elif value.upper() == 'TRUE':
        h = True
    bpy.context.object.rigid_body.use_start_deactivated = h

def rigidbody_dynamics_deactivation_velocity(value):
    val = float(value)
    bpy.context.object.rigid_body.deactivate_linear_velocity = val

def rigidbody_dynamics_deactivation_angular(value):
    val = float(value)
    bpy.context.object.rigid_body.deactivate_angular_velocity = val

