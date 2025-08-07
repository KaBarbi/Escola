from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaEstudanteSerializer, ListaMatriculasCursoSerializer
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk'])

    serializer_class = ListaMatriculaEstudanteSerializer


class ListaMatriculaCurso(generics.ListAPIView):
    serializer_class = ListaMatriculasCursoSerializer

    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk'])
