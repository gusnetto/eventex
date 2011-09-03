# -*- coding: utf-8 -*- 

import datetime
from django.contrib import admin
from subscription.models import Subscription
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext


class SubscriptionAdmin(admin.ModelAdmin):
	
	list_display  = ('name', 'email', 'phone', 'created_at', 'subscription_today', 'paid')		
	date_hierarchy = 'created_at' 	
	search_fields = ('name', 'cpf', 'email', 'phone', 'created_at') 	
	list_filter = ('paid', )

	actions = ['mark_as_paid']

	def mark_as_paid (self, request, queryset):
		count = queryset.update(paid=True)

		msg=ungettext(
			u'%(count)d inscricao foi marcada como paga.',
			u'%(count)d inscrições foram marcadas como pagas.',
			count

		)% {'count': count}
		self.message_user(request, msg)
	mark_as_paid.short_description = _(u"Marcar como pagas")

	def subscribed_today(self, obj):
		return obj.created_at.date() == datetime.date.today()
	subscribed_today.short_description = 'Inscrito hoje ?'
	subscribed_today.boolean = True

admin.site.register(Subscription, SubscriptionAdmin)
