class Plot(object):
    def __init__(self,name,array_func,event_weight_func,hist,
            dim=1,
            ):
        self.name = name
        self.array_func = array_func
        self.event_weight_func = event_weight_func
        self.hist = hist
        self.dim = dim

        self.data_color = 'black'
