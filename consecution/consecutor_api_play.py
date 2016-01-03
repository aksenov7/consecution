class Consecutor:
    def __init__(self, node):
        pass




####################################################################
####################################################################
# It would be nice if the api to consecutors was all in the "sync" world
# hiding all the async stuff inside.
####################################################################
####################################################################


# will have to think about how timeouts play with output generators
cons1 = Consecutor(node1, timeout=time_delta_or_relative_delta)
cons2 = Consecutor(node2, output_spooled_to_disk=False)

cons1.consume(iterable, 'port1') # this blocks until all input is completely acked or timeout
cons1.push(value, 'port1') # this blocks until value is completely acked  or timeout


# acking is done once item is placed into output iterable
# generators are read-once.  They can only be gotten once.
gen = cons1.get_generator('port1')


# consecutor always has one port for iterating over unprocessed values
cons1.has_unprocessed # true/false
unprocessed_gen = cons1.get_generator('unprocessed')





