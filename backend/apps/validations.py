from django.core.validators import RegexValidator

PHONE_NUMBER_REGEX = RegexValidator(
	r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$',
	"Only valid phone number in the format: '+999999999' is required")