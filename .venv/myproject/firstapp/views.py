from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import ClientForm, ProjectForm
from .models import Client, Project, ProjectAssignment
from django.contrib.auth.models import User
from django.contrib import messages

@login_required
def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

@login_required
def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    projects = client.projects.all()  # Fetch all projects related to the client
    return render(request, 'client_detail.html', {'client': client, 'projects': projects})

@login_required
def edit_client(request, id):
    client = get_object_or_404(Client, id=id)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'client_form.html', {'form': form})

@login_required
def delete_client(request, id):
    client = get_object_or_404(Client, id=id)
    client.delete()
    return redirect('client_list')


@login_required
def add_project(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)  # Avoids immediate save
            project.client = client  # Link to the client
            project.save()  # Save project with the client ID
            messages.success(request, "Project added successfully.")
            return redirect('client_detail', client_id=client.id)
        else:
            messages.error(request, "There was an error in the form submission.")
    else:
        form = ProjectForm()

    return render(request, 'add_project.html', {'form': form, 'client': client})


@login_required
def assign_project(request):
    if request.method == 'POST':
        # Log the request data
        print(request.POST)

        form = ProjectAssignmentForm(request.POST)

        if form.is_valid():
            # Validate and save the assignment
            project_assignment = form.save(commit=False)
            project_assignment.user = request.user  # or however you assign the user
            project_assignment.save()
            return redirect('success_url')  # Redirect after successful assignment
        else:
            # Handle the case where the form is not valid
            print(form.errors)  # Log form errors for debugging

    else:
        form = ProjectAssignmentForm()

    return render(request, 'assign_project.html', {'form': form})
@login_required
def assigned_projects(request):
    assignments = ProjectAssignment.objects.filter(user=request.user)
    print(assignments)
    return render(request, 'assigned_projects.html', {'assignments': assignments})

@login_required
def client_projects(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    projects = Project.objects.filter(client=client)
    return render(request, 'clients_projects.html', {'client': client, 'projects': projects})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
