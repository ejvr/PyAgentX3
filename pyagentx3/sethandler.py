# -*- coding: utf-8 -*-

# --------------------------------------------
import logging


class NullHandler(logging.Handler):
    def emit(self, record):
        pass


logger = logging.getLogger('pyagentx3.sethandler')
logger.addHandler(NullHandler())
# --------------------------------------------


class SetHandlerError(Exception):
    pass


class SetHandler():

    def __init__(self):
        self.transactions = {}

    def network_test(self, session_id, transaction_id, oid, data):
        tid = SetHandler._get_tid(session_id, transaction_id)
        try:
            self.test(oid, data)
            self.transactions[tid] = oid, data
        except SetHandlerError as e:
            self.transactions.pop(tid)
            logger.error('TestSet failed: %s', e)
            raise e

    def network_commit(self, session_id, transaction_id):
        tid = SetHandler._get_tid(session_id, transaction_id)
        try:
            oid, data = self.transactions.get(tid, (None, None))
            if oid is None:
                return
            self.commit(oid, data)
            self.transactions.pop(tid)
        except Exception as e:
            logger.error('CommitSet failed: %s', e)

    def network_undo(self, session_id, transaction_id):
        self.network_cleanup(session_id, transaction_id)

    def network_cleanup(self, session_id, transaction_id):
        tid = SetHandler._get_tid(session_id, transaction_id)
        self.transactions.pop(tid)

    @staticmethod
    def _get_tid(session_id, transaction_id):
        return f"{session_id}_{transaction_id}"

    # User override these
    def test(self, oid, data):
        pass

    def commit(self, oid, data):
        pass
