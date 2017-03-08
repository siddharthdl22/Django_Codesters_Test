from mongoengine import EmbeddedDocument, Document, fields, EmbeddedDocumentField

class Lesson(EmbeddedDocument):
    lesson_id = fields.StringField()
    lesson_name = fields.StringField()
    lesson_avggrade = fields.StringField()
    lesson_completecount = fields.IntField()
    lesson_incompletecount = fields.IntField()

class Error(EmbeddedDocument):
    error_type = fields.StringField()
    error_count = fields.IntField()
    error_studentcount = fields.IntField()

class Module(EmbeddedDocument):
    module_id = fields.StringField()
    module_name = fields.StringField()
    module_toppers = fields.StringField()
    errors = fields.ListField(EmbeddedDocumentField(Error))
    lessons = fields.ListField(EmbeddedDocumentField(Lesson))

class Teacher(Document):
    teacher_id = fields.StringField()
    modules = fields.ListField(EmbeddedDocumentField(Module))
    meta = {'strict': False}
