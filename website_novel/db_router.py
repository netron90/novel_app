# # db_router.py

# class TestRouter:
#     def db_for_read(self, model, **hints):
#         return 'default'

#     def db_for_write(self, model, **hints):
#         return 'default'

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if db == 'default':
#             return True
#         return None

# class ProductionRouter:
#     def db_for_read(self, model, **hints):
#         return 'postgres'

#     def db_for_write(self, model, **hints):
#         return 'postgres'

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if db == 'postgres':
#             return True
#         return None
    
# class AdminRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'admin':
#             return 'postgres'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'admin':
#             return 'postgres'
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'admin':
#             return db == 'postgres'
#         return None


# class AdminRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'admin':
#             return 'postgres'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'admin':
#             return 'postgres'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'admin':
#             return db == 'postgres'
#         return None

#-------------
# class TestRouter:
#     def db_for_read(self, model, **hints):
#         return 'default'

#     def db_for_write(self, model, **hints):
#         return 'default'

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if db == 'default':
#             return True
#         return None

# class ProductionRouter:
#     def db_for_read(self, model, **hints):
#         return 'postgres'

#     def db_for_write(self, model, **hints):
#         return 'postgres'

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if db == 'postgres':
#             return True
#         return None

# class AdminRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'admin' or model._meta.app_label == 'auth':
#             return 'postgres'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'admin' or model._meta.app_label == 'auth':
#             return 'postgres'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         if obj1._meta.app_label in ['admin', 'auth'] or \
#            obj2._meta.app_label in ['admin', 'auth']:
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in ['admin', 'auth']:
#             return db == 'postgres'
#         return None

# ----------------------------------------------------------------------

# class DatabaseRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'auth' or model._meta.app_label == 'admin':
#             return 'postgres'
#         return 'default'

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'auth' or model._meta.app_label == 'admin':
#             return 'postgres'
#         return 'default'

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'auth' or app_label == 'admin':
#             return db == 'postgres'
#         return db == 'default'

# ----------------------------------------------------------------------

# class AuthRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
#             return 'postgres'
#         return 'default'

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
#             return 'postgres'
#         return 'default'

#     def allow_relation(self, obj1, obj2, **hints):
#         if obj1._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin'] or \
#            obj2._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
#             return db == 'postgres'
#         return None

# ------------------------------------------------------------------------

class TestRouter:
    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'default':
            return True
        return None

class ProductionRouter:
    def db_for_read(self, model, **hints):
        return 'postgres'

    def db_for_write(self, model, **hints):
        return 'postgres'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'postgres':
            return True
        return None

class AdminRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'admin':
            return 'postgres'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'admin':
            return 'postgres'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'admin':
            return db == 'postgres'
        return None

# class AuthRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
#             return 'postgres'
#         return 'default'

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
#             return 'postgres'
#         return 'default'

#     def allow_relation(self, obj1, obj2, **hints):
#         if obj1._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin'] or \
#            obj2._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
#             return db == 'postgres'
#         return None

class AuthRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
            return 'postgres'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
            return 'postgres'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin'] or \
            obj2._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
            return db == 'postgres'
        return None


