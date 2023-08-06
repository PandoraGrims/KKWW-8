from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.html import urlencode
from web_forum.form import SearchForm, DiscussionForm, UserForm
from web_forum.models import Discussion
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


class DiscusListView(ListView):
    model = Discussion
    template_name = 'discus/discus_list.html'
    context_object_name = 'discussions'
    ordering = ("-created_at",)
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["form"] = self.form
        if self.search_value:
            context["query"] = urlencode({'search': self.search_value})
            context["search_value"] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        search_value = self.request.GET.get('search')
        if search_value:
            queryset = queryset.filter(Q(name__icontains=search_value) | Q(description__icontains=search_value))
        return queryset


class DiscusDetailView(DetailView):
    model = Discussion
    template_name = 'discus/discus_detail_view.html'
    context_object_name = 'discus'

    def get_success_url(self):
        return reverse("web_forum:discus_detail_view", kwargs={"pk": self.object.pk})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     discus = self.get_object()
    #     answers = discus.answers.all()
    #     context['answers'] = answers
    #     return context
#
#
# class ProjectCreateView(LoginRequiredMixin, CreateView):
#     model = Project
#     form_class = ProjectForm
#     template_name = "discus/project_create_view.html"
#
#     def get_success_url(self):
#         return reverse("web_forum:project_detail_view", kwargs={"pk": self.object.pk})
#
#
# class ProjectUpdateView(LoginRequiredMixin, UpdateView):
#     model = Project
#     form_class = ProjectForm
#     template_name = "discus/discus_update_view.html"
#
#     def get_success_url(self):
#         return reverse("web_forum:project_detail_view", kwargs={"pk": self.object.pk})
#
#
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
#
#
# class TaskCreateView(LoginRequiredMixin, CreateView):
#     form_class = TaskForm
#     template_name = "answers/create_task.html"
#     success_url = reverse_lazy("web_forum:task_view")
#
#     def get_success_url(self):
#         return reverse("web_forum:task_view", kwargs={"pk": self.object.pk})
#
#     def form_valid(self, form):
#         project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
#         task = form.save(commit=False)
#         task.project = project
#         task.save()
#         return redirect("web_forum:project_detail_view", pk=project.pk)
#
#
# class TaskUpdateView(LoginRequiredMixin, UpdateView):
#     model = Task
#     form_class = TaskForm
#     template_name = "answers/update_task.html"
#     success_url = reverse_lazy("web_forum:task_view")
#
#     def get_success_url(self):
#         return reverse("web_forum:task_view", kwargs={"pk": self.object.pk})
#
#
# class TaskDeleteView(LoginRequiredMixin, DeleteView):
#     model = Task
#     template_name = "answers/delete_task.html"
#     success_url = reverse_lazy("web_forum:index")
#
#
# class AddUserToProjectView(View):
#     def get(self, request, pk):
#         project = get_object_or_404(Project, pk=pk)
#         form = UserForm()
#         return render(request, 'user/add_user_to_project.html', {'discus': project, 'form': form})
#
#     def post(self, request, pk):
#         project = get_object_or_404(Project, pk=pk)
#         form = UserForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             user = get_object_or_404(User, username=username)
#             project.user.add(user)
#             return redirect('project_detail', pk=pk)
#         return render(request, 'user/add_user_to_project.html', {'discus': project, 'form': form})

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
