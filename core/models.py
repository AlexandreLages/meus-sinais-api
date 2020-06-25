from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    SEXO_CHOICES = {
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("O", "Outro")
    }

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=255, null=False)
    telefone_celular = models.CharField(max_length=255, null=True, default='')
    telefone_fixo = models.CharField(max_length=255, null=True, default='')
    cpf = models.CharField(max_length=255, null=True, default='')
    rg = models.CharField(max_length=255, null=True, default='')
    email = models.CharField(max_length=255, null=True, default='')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True)

    class Meta:
        db_table = 'tbUsuario'


class Colaborador(Usuario):
    crp = models.CharField(max_length=50, null=False)
    perfil = models.TextField(default='')
    verificado = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='imagens/', default='imagens/None/no-img.jpg')

    class Meta:
        db_table = 'tbColaborador'


class Especialidade(models.Model):
    nome = models.CharField(max_length=255, null=False, default='')
    descricao = models.CharField(max_length=255, null=True, default='')
    colaboradores = models.ManyToManyField(Colaborador)

    class Meta:
        db_table = 'tbEspecialidade'


class Horario(models.Model):
    SEMANA_CHOICES = {
        (1, "Domingo"),
        (2, "Segunda-Feira"),
        (3, "Terça-Feira"),
        (4, "Quarta-Feira"),
        (5, "Quinta-Feira"),
        (6, "Sexta-Feira"),
        (7, "Sábado"),
    }

    dia = models.CharField(max_length=1, choices=SEMANA_CHOICES, null=False)
    hora = models.CharField(max_length=5, null=False)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.DO_NOTHING, related_name = 'horarios')

    class Meta:
        db_table = 'tbHorario'


class Paciente(Usuario):
    ORIENTACAO_CHOICES = {
        ("HETERO", "Heterossexual"),
        ("HOMO", "Homossexual"),
        ("BI", "Bissexual"),
        ("INDEFINIDO", "Prefiro não informar")
    }

    data_nascimento = models.DateField(null=True)
    orientacao_sexual = models.CharField(max_length=10, choices=ORIENTACAO_CHOICES, null=True)

    class Meta:
        db_table = 'tbPaciente'


class Administrador(Usuario):

    class Meta:
        db_table = 'tbAdministrador'


class Agendamento(models.Model):
    STATUS_CHOICES = {
        ("ANALISE", "Em Análise"),
        ("ACEITO", "Aceito"),
        ("REALIZADO", "Realizado"),
        ("CANCELADO", "Cancelado"),
    }

    TIPO_CHOICES = {
        ("PLANTAO", "Plantão"),
        ("PSICOTERAPIA", "Psicoterapia"),
    }

    data = models.DateField(null=False)
    horario = models.CharField(max_length=5, null=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=False)
    motivo = models.CharField(max_length=255, null=False)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, null=False)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.DO_NOTHING, related_name = 'agendamentos', null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING, related_name = 'agendamentos', null=True)

    class Meta:
        db_table = 'tbAgendamento'