
class QueueSolutionEntrypoint:

    def enqueue(self, task):
        raise NotImplementedError()

    def dequeue(self):
        raise NotImplementedError()

    def size(self):
        raise NotImplementedError()

    def purge(self):
        raise NotImplementedError()
