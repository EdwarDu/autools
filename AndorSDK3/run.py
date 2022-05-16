from pyandor3 import Andor3Man

a3man = Andor3Man()

#a3man.register_feature_cb("F1", lambda f: print(f"What the Callback {f}"))
#a3man.set_s_feature("F1", "ssss")

#buffer_id = a3man.create_buffer(10240)
#a3man.queue_buffer(buffer_id)
#buffer_id_g, buffer_readout_size = a3man.wait_buffer(1000)

#print(a3man.get_data_from_buffer(buffer_id_g, buffer_readout_size))

