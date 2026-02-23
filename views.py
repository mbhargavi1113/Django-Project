from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Complaint
from .serializers import ComplaintSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def complaint_list(request):
    if request.method == 'GET':
        ordering = request.query_params.get('ordering')
        search = request.query_params.get('search')
        complaints = Complaint.objects.all()
        priority = request.query_params.get('priority')
        category = request.query_params.get('category')
        title = request.query_params.get('title')
        # Filtering
        if priority:
            complaints = complaints.filter(priority__iexact=priority)
        if category:
            complaints = complaints.filter(category__icontains=category)
        if title:
            complaints = complaints.filter(title__icontains=title)
        # Search (simple)
        if search:
            complaints = complaints.filter(title__icontains=search)
        # Ordering
        if ordering:
            complaints = complaints.order_by(ordering)
        # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 2
        paginated_complaints = paginator.paginate_queryset(complaints, request)
        serializer = ComplaintSerializer(paginated_complaints, many=True)
        return paginator.get_paginated_response(serializer.data)
    if request.method == 'POST':
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@cache_page(60)
@permission_classes([IsAuthenticated])
def complaint_detail(request, id):
    try:
        complaint = Complaint.objects.get(id=id)
    except Complaint.DoesNotExist:
        return Response({'error': 'Complaint not found'}, status=404)
    if request.method == 'GET':
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ComplaintSerializer(complaint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    if request.method == 'PATCH':
        serializer = ComplaintSerializer(complaint, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    if request.method == 'DELETE':
        complaint.delete()
        return Response({'message': 'Complaint deleted successfully'})
# Create your views here.
