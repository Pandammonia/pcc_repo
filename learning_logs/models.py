from django.db import models

class Topic(models.Model):
	"""A topic about what user is learning"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return a string rep of model"""
		return self.text

class Entry(models.Model):
	"""Something specific learned about models"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		if len(self.text) > 50:
			return f"{self.text[:50]}..."
		else:
			return f"{self.text}"


