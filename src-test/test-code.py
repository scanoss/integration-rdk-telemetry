

def add_to_queue(self, id):
    if id in self.last_queued:
        logger.debug(f"ID {id} is in last_queued")
        if self.last_queued[id] + self.settings.prevent_requeuing_time > time.time():
            logger.debug(f"Skipping {id}: added too recently.")
            return False
logger.debug(f"Adding {id} to queue.")
self.last_queued[id] = time.time()
self.queue.put(id, True, self.settings.queue_interaction_timeout)
return True

