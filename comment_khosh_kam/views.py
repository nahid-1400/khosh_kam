from comment_khosh_kam.models import Comment
from comment_khosh_kam.forms import CommentForm
from django.shortcuts import reverse, redirect
import sweetify

def add_comment(request, malile_id):
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        user_name = comment_form.cleaned_data.get('user_name')
        text_comment = comment_form.cleaned_data.get('text_comment')
        email_comment = comment_form.cleaned_data.get('email_comment')
        Comment.objects.create(malile_id=malile_id, user_name=user_name, user_ip_address=request.user.ip_address,
                               text_comment=text_comment, email_comment=email_comment)
        sweetify.success(request, 'موفقیت', text='نظر شما با موفقیا ثبت شد و بعد از تایید ادمین سایت منتشر میشود', persistent='باشه')
        return redirect(reverse("malile_khosh_kam:malile_detail", args=[malile_id]))
