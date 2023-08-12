from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404, reverse

from django.core.paginator import Paginator

from web_forum.form import DiscussionForm, AnswerForm
from web_forum.models import Discussion, Answer
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class DiscusListView(ListView):
    model = Discussion
    template_name = 'discus/discus_list.html'
    context_object_name = 'discussions'
    ordering = ("-created_at",)
    paginate_by = 4


class DiscusDetailView(DetailView):
    model = Discussion
    template_name = 'discus/discus_detail_view.html'
    context_object_name = 'discus'
    answers_paginate_by = 4

    def get_success_url(self):
        return reverse("web_forum:discus_detail_view", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        discus = self.get_object()

        answers = discus.answers.all().order_by('-created_at')
        paginator = Paginator(answers, self.answers_paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['answers'] = page_obj
        return context


class DiscusCreateView(LoginRequiredMixin, CreateView):
    model = Discussion
    form_class = DiscussionForm
    template_name = "discus/discus_create_view.html"

    def get_success_url(self):
        return reverse("web_forum:discus_detail_view", kwargs={"pk": self.object.pk})


class DiscusUpdateView(LoginRequiredMixin, UpdateView):
    model = Discussion
    form_class = DiscussionForm
    template_name = "discus/discus_update_view.html"

    def get_success_url(self):
        return reverse("web_forum:discus_detail_view", kwargs={"pk": self.object.pk})


class UserProfileDetailView(DetailView):
    model = User
    template_name = 'user/user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        if not self.request.user.is_authenticated:
            raise Http404
        return get_object_or_404(User, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        discussions = Discussion.objects.filter(author=user)
        total_answers = Answer.objects.filter(discussion__author=user).count()

        context['discussions'] = discussions
        context['total_answers'] = total_answers
        return context

# class ProjectDeleteView(LoginRequiredMixin, DeleteView):
#     model = Project
#     template_name = "discus/project_delete_view.html"
#     success_url = reverse_lazy("web_forum:index")
#
#
# class TaskDetailView(DetailView):
#     model = Task
#     template_name = 'answers/task.html'
#     context_object_name = 'task'

# class TaskCreateView(LoginRequiredMixin, CreateView):
#     form_class = TaskForm
#     template_name = "tasks/create_task.html"
#     success_url = reverse_lazy("webapp:task_view")
#
#     def get_success_url(self):
#         return reverse("webapp:task_view", kwargs={"pk": self.object.pk})
#
#     def form_valid(self, form):
#         project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
#         task = form.save(commit=False)
#         task.project = project
#         task.save()
#         return redirect("webapp:project_detail_view", pk=project.pk)


class AnswerCreateView(LoginRequiredMixin, CreateView):
    # model = Answer
    # form_class = AnswerForm
    # template_name = "answers/create_answer.html"
    # success_url = reverse_lazy("web_forum:answer_add")
    #
    # def get_success_url(self):
    #     return reverse("web_forum:discus_detail_view", kwargs={"pk": self.object.pk})
    #
    # def form_valid(self, form):
    #     discus = get_object_or_404(Discussion, pk=self.kwargs.get("pk"))
    #     answer = form.save(commit=False)
    #     answer.discus = discus
    #     answer.save()
    #     return redirect("web_forum:discus_detail_view", pk=discus.pk)

    model = Answer
    form_class = AnswerForm
    template_name = "answers/create_answer.html"

    def get_success_url(self):
        return reverse("web_forum:discus_detail_view", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        discus = get_object_or_404(Discussion, pk=self.kwargs.get("pk"))
        answer = form.save(commit=False)
        answer.discus = discus
        answer.save()
        return redirect("web_forum:discus_detail_view", pk=discus.pk)

# class TaskUpdateView(LoginRequiredMixin, UpdateView):
#     model = Task
#     form_class = TaskForm
#     template_name = "answers/update_answer.html"
#     success_url = reverse_lazy("web_forum:task_view")
#
#     def get_success_url(self):
#         return reverse("web_forum:task_view", kwargs={"pk": self.object.pk})
#
#
# class TaskDeleteView(LoginRequiredMixin, DeleteView):
#     model = Task
#     template_name = "answers/delete_answer.html"
#     success_url = reverse_lazy("web_forum:index")
#
#
# class AddUserToProjectView(View):
#     def get(self, request, pk):
#         discus = get_object_or_404(Discussion, pk=pk)
#         form = AnswerForm()
#         return render(request, 'answer_form.html', {'discus': discus, 'form': form})
#
#     def post(self, request, pk):
#         discus = get_object_or_404(Discussion, pk=pk)
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['name']
#             answer = get_object_or_404(User, username=username)
#             discus.answers.add(answer)
#             return redirect('web_forum:discus_detail_view', pk=pk)
#         return render(request, 'answer_form.html', {'discus': discus, 'form': form})

# class RemoveUserFromProjectView(View):
#     def get(self, request, pk, user_pk):
#         discus = get_object_or_404(Project, pk=pk)
#         user = get_object_or_404(User, pk=user_pk)
#         return render(request, 'discus/remove_user_from_project.html', {'discus': discus, 'user': user})
#
#     def post(self, request, pk, user_pk):
#         discus = get_object_or_404(Project, pk=pk)
#         user = get_object_or_404(User, pk=user_pk)
#         discus.members.remove(user)
#         return redirect('project_detail', pk=pk)
