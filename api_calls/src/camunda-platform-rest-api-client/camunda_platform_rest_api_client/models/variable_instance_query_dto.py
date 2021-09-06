from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.variable_instance_query_dto_sorting_item import VariableInstanceQueryDtoSortingItem
from ..models.variable_query_parameter_dto import VariableQueryParameterDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="VariableInstanceQueryDto")


@attr.s(auto_attribs=True)
class VariableInstanceQueryDto:
    """A variable instance query which defines a list of variable instances"""

    variable_name: Union[Unset, None, str] = UNSET
    variable_name_like: Union[Unset, None, str] = UNSET
    process_instance_id_in: Union[Unset, None, List[str]] = UNSET
    execution_id_in: Union[Unset, None, List[str]] = UNSET
    case_instance_id_in: Union[Unset, None, List[str]] = UNSET
    case_execution_id_in: Union[Unset, None, List[str]] = UNSET
    task_id_in: Union[Unset, None, List[str]] = UNSET
    batch_id_in: Union[Unset, None, List[str]] = UNSET
    activity_instance_id_in: Union[Unset, None, List[str]] = UNSET
    tenant_id_in: Union[Unset, None, List[str]] = UNSET
    variable_values: Union[Unset, None, List[VariableQueryParameterDto]] = UNSET
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET
    sorting: Union[Unset, List[VariableInstanceQueryDtoSortingItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        variable_name = self.variable_name
        variable_name_like = self.variable_name_like
        process_instance_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.process_instance_id_in, Unset):
            if self.process_instance_id_in is None:
                process_instance_id_in = None
            else:
                process_instance_id_in = self.process_instance_id_in

        execution_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.execution_id_in, Unset):
            if self.execution_id_in is None:
                execution_id_in = None
            else:
                execution_id_in = self.execution_id_in

        case_instance_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.case_instance_id_in, Unset):
            if self.case_instance_id_in is None:
                case_instance_id_in = None
            else:
                case_instance_id_in = self.case_instance_id_in

        case_execution_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.case_execution_id_in, Unset):
            if self.case_execution_id_in is None:
                case_execution_id_in = None
            else:
                case_execution_id_in = self.case_execution_id_in

        task_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.task_id_in, Unset):
            if self.task_id_in is None:
                task_id_in = None
            else:
                task_id_in = self.task_id_in

        batch_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.batch_id_in, Unset):
            if self.batch_id_in is None:
                batch_id_in = None
            else:
                batch_id_in = self.batch_id_in

        activity_instance_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.activity_instance_id_in, Unset):
            if self.activity_instance_id_in is None:
                activity_instance_id_in = None
            else:
                activity_instance_id_in = self.activity_instance_id_in

        tenant_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tenant_id_in, Unset):
            if self.tenant_id_in is None:
                tenant_id_in = None
            else:
                tenant_id_in = self.tenant_id_in

        variable_values: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.variable_values, Unset):
            if self.variable_values is None:
                variable_values = None
            else:
                variable_values = []
                for variable_values_item_data in self.variable_values:
                    variable_values_item = variable_values_item_data.to_dict()

                    variable_values.append(variable_values_item)

        variable_names_ignore_case = self.variable_names_ignore_case
        variable_values_ignore_case = self.variable_values_ignore_case
        sorting: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sorting, Unset):
            sorting = []
            for sorting_item_data in self.sorting:
                sorting_item = sorting_item_data.to_dict()

                sorting.append(sorting_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variable_name is not UNSET:
            field_dict["variableName"] = variable_name
        if variable_name_like is not UNSET:
            field_dict["variableNameLike"] = variable_name_like
        if process_instance_id_in is not UNSET:
            field_dict["processInstanceIdIn"] = process_instance_id_in
        if execution_id_in is not UNSET:
            field_dict["executionIdIn"] = execution_id_in
        if case_instance_id_in is not UNSET:
            field_dict["caseInstanceIdIn"] = case_instance_id_in
        if case_execution_id_in is not UNSET:
            field_dict["caseExecutionIdIn"] = case_execution_id_in
        if task_id_in is not UNSET:
            field_dict["taskIdIn"] = task_id_in
        if batch_id_in is not UNSET:
            field_dict["batchIdIn"] = batch_id_in
        if activity_instance_id_in is not UNSET:
            field_dict["activityInstanceIdIn"] = activity_instance_id_in
        if tenant_id_in is not UNSET:
            field_dict["tenantIdIn"] = tenant_id_in
        if variable_values is not UNSET:
            field_dict["variableValues"] = variable_values
        if variable_names_ignore_case is not UNSET:
            field_dict["variableNamesIgnoreCase"] = variable_names_ignore_case
        if variable_values_ignore_case is not UNSET:
            field_dict["variableValuesIgnoreCase"] = variable_values_ignore_case
        if sorting is not UNSET:
            field_dict["sorting"] = sorting

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        variable_name = d.pop("variableName", UNSET)

        variable_name_like = d.pop("variableNameLike", UNSET)

        process_instance_id_in = cast(List[str], d.pop("processInstanceIdIn", UNSET))

        execution_id_in = cast(List[str], d.pop("executionIdIn", UNSET))

        case_instance_id_in = cast(List[str], d.pop("caseInstanceIdIn", UNSET))

        case_execution_id_in = cast(List[str], d.pop("caseExecutionIdIn", UNSET))

        task_id_in = cast(List[str], d.pop("taskIdIn", UNSET))

        batch_id_in = cast(List[str], d.pop("batchIdIn", UNSET))

        activity_instance_id_in = cast(List[str], d.pop("activityInstanceIdIn", UNSET))

        tenant_id_in = cast(List[str], d.pop("tenantIdIn", UNSET))

        variable_values = []
        _variable_values = d.pop("variableValues", UNSET)
        for variable_values_item_data in _variable_values or []:
            variable_values_item = VariableQueryParameterDto.from_dict(variable_values_item_data)

            variable_values.append(variable_values_item)

        variable_names_ignore_case = d.pop("variableNamesIgnoreCase", UNSET)

        variable_values_ignore_case = d.pop("variableValuesIgnoreCase", UNSET)

        sorting = []
        _sorting = d.pop("sorting", UNSET)
        for sorting_item_data in _sorting or []:
            sorting_item = VariableInstanceQueryDtoSortingItem.from_dict(sorting_item_data)

            sorting.append(sorting_item)

        variable_instance_query_dto = cls(
            variable_name=variable_name,
            variable_name_like=variable_name_like,
            process_instance_id_in=process_instance_id_in,
            execution_id_in=execution_id_in,
            case_instance_id_in=case_instance_id_in,
            case_execution_id_in=case_execution_id_in,
            task_id_in=task_id_in,
            batch_id_in=batch_id_in,
            activity_instance_id_in=activity_instance_id_in,
            tenant_id_in=tenant_id_in,
            variable_values=variable_values,
            variable_names_ignore_case=variable_names_ignore_case,
            variable_values_ignore_case=variable_values_ignore_case,
            sorting=sorting,
        )

        variable_instance_query_dto.additional_properties = d
        return variable_instance_query_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
