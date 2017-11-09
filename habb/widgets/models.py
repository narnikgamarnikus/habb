import uuid
from django.db import models
from django.conf import settings
from pygments.styles import get_all_styles
from pygments.lexers import get_all_lexers
from django.core.urlresolvers import reverse
from model_utils import Choices, FieldTracker
from django.utils.translation import ugettext_lazy as _
from model_utils.fields import StatusField, MonitorField
from django.utils.encoding import python_2_unicode_compatible
from model_utils.models import TimeStampedModel, SoftDeletableModel
from django.contrib.postgres.fields import ArrayField
from model_utils.fields import StatusField, MonitorField
from django.utils.functional import cached_property
from annoying.functions import get_object_or_None
from .utils import token_generator
from django.core.exceptions import ValidationError



LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


@python_2_unicode_compatible
class Base(SoftDeletableModel, TimeStampedModel):
	
	tracker = FieldTracker()

	class Meta:
		abstract = True


@python_2_unicode_compatible
class Website(Base):

	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('widgets.website_detail', kwargs={'pk': self.pk})

'''
python_2_unicode_compatible
class Competition(Base):
	
	STATUS = Choices(
		('active', 'active', _('Active')), 
		('complete', 'complete', _('Complete'))
	)

	status = StatusField(
		choices=STATUS, 
		default=STATUS.active,
		max_length=20
	)

	winner = models.ForeignKey('widgets.Leed')

	def __str__(self):
		return str(self.pk)
'''


@python_2_unicode_compatible
class Widget(Base):

	STATUS = Choices(
		('work', 'work', _('Work')), 
		('stoped', 'stoped', _('Stoped')),
		('end', 'end', _('End'))
	)

	COMPETITIONS_TYPE = Choices(
		('random', 'random', _('Random')),
		('leeds', 'leeds', _('Leeds')) 
	)

	COMPETITIONS_STATUS = Choices(
		('soon', 'soon', _('Coming soon')),
		('active', 'active', _('Active')), 
		('complete', 'complete', _('Complete'))
	)
	
	FIELDS = Choices(
		('email', 'email', _('Email')),
		('phone_number', 'phone_number', _('phone_number')),
		('first_name', 'first_name', _('First name')),
		('last_name', 'last_name', _('Last name')),
		('first_name', 'first_name', _('First name'))
	)

	steps = models.PositiveSmallIntegerField(default=3, blank=True)

	#competition = models.ForeignKey(
	#	'widgets.Competition', 
	#	null=True,
	#	blank=True
	#)

	competition_type = models.CharField(
		choices=COMPETITIONS_TYPE,
		default=COMPETITIONS_TYPE.random,
		max_length=20,
		blank=True
	)

	competition_status = models.CharField(
		choices=COMPETITIONS_STATUS,
		default=COMPETITIONS_STATUS.soon,
		max_length=20,
		blank=True
	)

	status = StatusField(
		choices=STATUS, 
		default=STATUS.stoped,
		max_length=20,
		blank=True
	)
	
	title = models.CharField(max_length=50, null=True, blank=True)
	offer = models.CharField(max_length=50, null=True, blank=True)
	text = models.CharField(max_length=100, null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	button_text = models.CharField(max_length=50, null=True, blank=True)
	button_color = models.CharField(max_length=50, null=True, blank=True)

	#telegram = models.CharField(max_length=50)

	winner = models.ForeignKey('widgets.Leed', null=True, related_name='winner', blank=True)


	fields = models.CharField(#ArrayField(
		choices=STATUS, 
		default=STATUS.stoped,
		max_length=20),
		#)

	website = models.ForeignKey(Website, null=True)
	token = models.CharField(max_length=100, null=True, blank=True)

	date_start = models.DateTimeField(null=True)
	date_end = models.DateTimeField(null=True)

	viewed = models.PositiveSmallIntegerField(default=0)
	opened = models.PositiveSmallIntegerField(default=0)
	closed = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return '{}'.format(self.token)

	def create_competition(self):
		if self.status == 'end':
			competition = Competition.objects.create()
			self.competition = competition
			self.save()
		raise ValidationError('Widget must have end status')


	def generate_token(self):
		self.token = token_generator()
		self.save()

	def widget_script(self):
		return ''

	def get_absolute_url(self):
		return reverse('widgets.widget_detail', kwargs={'token': self.token})


	def save(self):
		if not self.token:
			self.generate_token()
		return super(Widget, self).save()



@python_2_unicode_compatible
class Link(Base):

	widget = models.ForeignKey(Widget, null=True)
	name = models.CharField(max_length=50, null=True)
	src = models.CharField(max_length=500, null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('widgets.link_detail', kwargs={'pk': self.pk})


@python_2_unicode_compatible
class Leed(Base):

	widget = models.ForeignKey(Widget, null=True)
	
	first_name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=True)
	phone_number = models.CharField(max_length=50, null=True)
	email = models.CharField(max_length=50, null=True)
	telegram = models.CharField(max_length=50, null=True)

	referal = models.CharField(max_length=50, null=True)
	token = models.UUIDField(default=uuid.uuid4, editable=False)

	def get_absolute_url(self):
		return reverse('widgets.leed_detail', kwargs={'pk': self.pk})
	
	@cached_property
	def email_sent(self):
		email = get_object_or_None(Email, leed=self, widget=self.widget)
		if email:
			return {
				"status": email.status,
				"last action": email.modifed
			}
		return None

	@cached_property
	def sms_sent(self):
		sms = get_object_or_None(SMS, leed=self, widget=self.widget)
		if sms:
			return {
				"status": sms.status,
				"last action": sms.modifed
			}

	@cached_property
	def telegram_sent(self):
		telegram = get_object_or_None(Telegram, leed=self, widget=self.widget)
		if telegram:
			return {
				"status": telegram.status,
				"last action": telegram.modifed
			}

	@cached_property
	def call_called(self):
		call = get_object_or_None(Call, leed=self, widget=self.widget)
		if call:
			return {
				"status": call.status,
				"last action": call.modifed
			}
	
	@cached_property
	def referals(self):
		return Leed.objects.filter(widget=self.widget, referal=self.token)

	@cached_property
	def refferer(self):
		return Leed.objects.filter(widget=self.widget, token=self.referal)

	@cached_property
	def full_name(self):
		return '{} {}'.format(
			self.first_name,
			self.last_name
			)

	def __str__(self):
		return '{} {}'.format(
			self.full_name,
			self.phone_number
			)


@python_2_unicode_compatible
class Schedule(TimeStampedModel):

	SENDING_FREQUENCY = Choices(
		_('One time'), _('Daily'), _('Weekly'), _('Monthly'), _('Yearly')
	)
	sending_frequency = StatusField(
		choices_name='SENDING_FREQUENCY',
		verbose_name=_('Frequency of sending')
	)
	datetime = models.DateTimeField(null=True)
	complete = models.BooleanField(default=False,
		verbose_name=_('Complete')
	)

	def get_absolute_url(self):
		return reverse('event_email:Schedule_detail', 
			kwargs={'pk': self.pk})


@python_2_unicode_compatible
class EmailMessage(Base):

	STATUS = Choices(
		_('Created'), _('Scheduled'),_('Sent'), _('Opened'), _('Clicked')
	)
	status = StatusField(verbose_name=_('Status'))

	widget = models.ForeignKey('widgets.Widget', null=True)
	leed = models.ForeignKey('widgets.Leed', null=True)
	
	subject = models.CharField(max_length=50, null=True)
	text = models.CharField(max_length=500, null=True)
	html = models.CharField(max_length=1000, null=True)

	status_changed = MonitorField(monitor='status')

	scheduled_at = MonitorField(monitor='status',
		when=['Sent'],
		verbose_name=_('Email scheduled at')
	)
	sent_at = MonitorField(monitor='status',
		when=['Scheduled'],
		verbose_name=_('Email sent at')
	)
	opened_at = MonitorField(monitor='status',
		when=['Opened'],
		verbose_name=_('Email opened at')
	)
	clicked_at = MonitorField(monitor='status',
		when=['Clicked'],
		verbose_name=_('Email clicked at')
	)

	def get_absolute_url(self):
		return reverse('widgets:email_detail', 
			kwargs={'pk': self.pk})


@python_2_unicode_compatible
class SMS(Base):

	STATUS = Choices(
		_('Created'), _('Scheduled'), _('Sent')
	)
	status = StatusField(verbose_name=_('Status'))

	widget = models.ForeignKey('widgets.Widget', null=True)
	leed = models.ForeignKey('widgets.Leed', null=True)
	
	subject = models.CharField(max_length=50, null=True)
	text = models.CharField(max_length=500, null=True)

	status_changed = MonitorField(monitor='status')

	scheduled_at = MonitorField(monitor='status',
		when=['Scheduled'],
		verbose_name=_('SMS sheduled at')
	)
	sent_at = MonitorField(monitor='status',
		when=['Sent'],
		verbose_name=_('SMS sent at')
	)

	def get_absolute_url(self):
		return reverse('widgets:email_detail', 
			kwargs={'pk': self.pk})


@python_2_unicode_compatible
class TelegramMessage(Base):

	STATUS = Choices(
		_('Created'), _('Scheduled'), _('Sent')
	)
	status = StatusField(verbose_name=_('Status'))

	widget = models.ForeignKey('widgets.Widget', null=True)
	leed = models.ForeignKey('widgets.Leed', null=True)
	
	message = models.CharField(max_length=500, null=True)

	status_changed = MonitorField(monitor='status')

	scheduled_at = MonitorField(monitor='status',
		when=['Scheduled'],
		verbose_name=_('SMS sheduled at')
	)
	sent_at = MonitorField(monitor='status',
		when=['Sent'],
		verbose_name=_('SMS sent at')
	)

	def get_absolute_url(self):
		return reverse('widgets:telegram_detail', 
			kwargs={'pk': self.pk})


@python_2_unicode_compatible
class Call(Base):

	STATUS = Choices(
		_('Created'), _('Scheduled'),_('Called')
	)
	status = StatusField(verbose_name=_('Status'))

	widget = models.ForeignKey('widgets.Widget', null=True)
	leed = models.ForeignKey('widgets.Leed', null=True)
	
	subject = models.CharField(max_length=50)
	text = models.CharField(max_length=500)
	file = models.FileField()

	status_changed = MonitorField(monitor='status')

	scheduled_at = MonitorField(monitor='status',
		when=['Sent'],
		verbose_name=_('Call scheduled at')
	)
	called_at = MonitorField(monitor='called',
		when=['Called'],
		verbose_name=_('Called at')
	)

	def get_absolute_url(self):
		return reverse('widgets:email_detail', 
			kwargs={'pk': self.pk})


@python_2_unicode_compatible
class Report(Base):
	
	widget = models.ForeignKey(Widget, null=True)


'''
@receiver(pixel_data)
def example_receiver(**kwargs):
	"""Example receiver of pixel_data signal."""
	pixel_data = kwargs['pixel_data']
	if pixel_data['content_type'] == 'Email':
		email = get_object_or_None(Email, pk = pixel_data['content_id'])
		if email:
			if email.token == pixel_data['token']:
				email.status == 'Opened'
				email.save()
'''