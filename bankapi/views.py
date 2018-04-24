from rest_framework import exceptions
from rest_framework.generics import ListAPIView
from .models import BankBranches
from .serializers import BankBranchesSerializer
from .pagination import BankPageNumberPagination
# Create your views here.
class BankBranchesList(ListAPIView):
    queryset_list = BankBranches.objects.all()
    serializer_class = BankBranchesSerializer
    def get_queryset(self, *args, **kwargs):
        ifsc = self.request.query_params.get('ifsc', None)
        bank_name = self.request.query_params.get('bank_name',None)
        city = self.request.query_params.get('city',None)
        bank_id = self.request.query_params.get('bank_id',None)
        branch = self.request.query_params.get('branch',None)
        address = self.request.query_params.get('address',None)
        district = self.request.query_params.get('district',None)
        state = self.request.query_params.get('state',None)

        if ifsc is not None:
            if((bank_id or branch or address or district or state or bank_name or city) is not None):
                raise exceptions.NotAcceptable(detail="other parameters cannot be applied with ifsc code")
            else:
                self.pagination_class = BankPageNumberPagination
                self.queryset_list = self.queryset_list.filter(ifsc=ifsc)
                if len(self.queryset_list) == 0:
                    raise exceptions.NotFound(detail="No bank with given ifsc code found in database")
                return self.queryset_list

        elif city is not None and bank_name is not None:
            if ((bank_id or branch or address or district or state or ifsc) is not None):
                raise exceptions.NotAcceptable(detail="other parameters cannot be applied "
                                                     "with bank_name and city")
            else:
                self.pagination_class = BankPageNumberPagination
                self.queryset_list = self.queryset_list.filter(bank_name=bank_name,
                                                           city=city)
                if len(self.queryset_list) == 0:
                    raise exceptions.NotFound(detail="No bank with given bank name and city found in database")
                return self.queryset_list

        else:
            raise exceptions.NotAcceptable(detail="Required parameters are missing. Please set any of the following parameters and try again:ifsc or bank_name and city", code= 'parametersMissing')
