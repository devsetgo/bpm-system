from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.execution_query_dto_sorting_item import ExecutionQueryDtoSortingItem
from ..models.variable_query_parameter_dto import VariableQueryParameterDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionQueryDto")


@attr.s(auto_attribs=True)
class ExecutionQueryDto:
    """A Execution instance query which defines a list of Execution instances"""

    business_key: Union[Unset, None, str] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    process_definition_key: Union[Unset, None, str] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    activity_id: Union[Unset, None, str] = UNSET
    signal_event_subscription_name: Union[Unset, None, str] = UNSET
    message_event_subscription_name: Union[Unset, None, str] = UNSET
    active: Union[Unset, None, bool] = UNSET
    suspended: Union[Unset, None, bool] = UNSET
    incident_id: Union[Unset, None, str] = UNSET
    incident_type: Union[Unset, None, str] = UNSET
    incident_message: Union[Unset, None, str] = UNSET
    incident_message_like: Union[Unset, None, str] = UNSET
    tenant_id_in: Union[Unset, None, List[str]] = UNSET
    variables: Union[Unset, None, List[VariableQueryParameterDto]] = UNSET
    process_variables: Union[Unset, None, List[VariableQueryParameterDto]] = UNSET
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET
    sorting: Union[Unset, List[ExecutionQueryDtoSortingItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        business_key = self.business_key
        process_definition_id = self.process_definition_id
        process_definition_key = self.process_definition_key
        process_instance_id = self.process_instance_id
        activity_id = self.activity_id
        signal_event_subscription_name = self.signal_event_subscription_name
        message_event_subscription_name = self.message_event_subscription_name
        active = self.active
        suspended = self.suspended
        incident_id = self.incident_id
        incident_type = self.incident_type
        incident_message = self.incident_message
        incident_message_like = self.incident_message_like
        tenant_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tenant_id_in, Unset):
            if self.tenant_id_in is None:
                tenant_id_in = None
            else:
                tenant_id_in = self.tenant_id_in

        variables: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.variables, Unset):
            if self.variables is None:
                variables = None
            else:
                variables = []
                for variables_item_data in self.variables:
                    variables_item = variables_item_data.to_dict()

                    variables.append(variables_item)

        process_variables: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.process_variables, Unset):
            if self.process_variables is None:
                process_variables = None
            else:
                process_variables = []
                for process_variables_item_data in self.process_variables:
                    process_variables_item = process_variables_item_data.to_dict()

                    process_variables.append(process_variables_item)

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
        if business_key is not UNSET:
            field_dict["businessKey"] = business_key
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if process_definition_key is not UNSET:
            field_dict["processDefinitionKey"] = process_definition_key
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if signal_event_subscription_name is not UNSET:
            field_dict["signalEventSubscriptionName"] = signal_event_subscription_name
        if message_event_subscription_name is not UNSET:
            field_dict["messageEventSubscriptionName"] = message_event_subscription_name
        if active is not UNSET:
            field_dict["active"] = active
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if incident_id is not UNSET:
            field_dict["incidentId"] = incident_id
        if incident_type is not UNSET:
            field_dict["incidentType"] = incident_type
        if incident_message is not UNSET:
            field_dict["incidentMessage"] = incident_message
        if incident_message_like is not UNSET:
            field_dict["incidentMessageLike"] = incident_message_like
        if tenant_id_in is not UNSET:
            field_dict["tenantIdIn"] = tenant_id_in
        if variables is not UNSET:
            field_dict["variables"] = variables
        if process_variables is not UNSET:
            field_dict["processVariables"] = process_variables
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
        business_key = d.pop("businessKey", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        process_definition_key = d.pop("processDefinitionKey", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        activity_id = d.pop("activityId", UNSET)

        signal_event_subscription_name = d.pop("signalEventSubscriptionName", UNSET)

        message_event_subscription_name = d.pop("messageEventSubscriptionName", UNSET)

        active = d.pop("active", UNSET)

        suspended = d.pop("suspended", UNSET)

        incident_id = d.pop("incidentId", UNSET)

        incident_type = d.pop("incidentType", UNSET)

        incident_message = d.pop("incidentMessage", UNSET)

        incident_message_like = d.pop("incidentMessageLike", UNSET)

        tenant_id_in = cast(List[str], d.pop("tenantIdIn", UNSET))

        variables = []
        _variables = d.pop("variables", UNSET)
        for variables_item_data in _variables or []:
            variables_item = VariableQueryParameterDto.from_dict(variables_item_data)

            variables.append(variables_item)

        process_variables = []
        _process_variables = d.pop("processVariables", UNSET)
        for process_variables_item_data in _process_variables or []:
            process_variables_item = VariableQueryParameterDto.from_dict(process_variables_item_data)

            process_variables.append(process_variables_item)

        variable_names_ignore_case = d.pop("variableNamesIgnoreCase", UNSET)

        variable_values_ignore_case = d.pop("variableValuesIgnoreCase", UNSET)

        sorting = []
        _sorting = d.pop("sorting", UNSET)
        for sorting_item_data in _sorting or []:
            sorting_item = ExecutionQueryDtoSortingItem.from_dict(sorting_item_data)

            sorting.append(sorting_item)

        execution_query_dto = cls(
            business_key=business_key,
            process_definition_id=process_definition_id,
            process_definition_key=process_definition_key,
            process_instance_id=process_instance_id,
            activity_id=activity_id,
            signal_event_subscription_name=signal_event_subscription_name,
            message_event_subscription_name=message_event_subscription_name,
            active=active,
            suspended=suspended,
            incident_id=incident_id,
            incident_type=incident_type,
            incident_message=incident_message,
            incident_message_like=incident_message_like,
            tenant_id_in=tenant_id_in,
            variables=variables,
            process_variables=process_variables,
            variable_names_ignore_case=variable_names_ignore_case,
            variable_values_ignore_case=variable_values_ignore_case,
            sorting=sorting,
        )

        execution_query_dto.additional_properties = d
        return execution_query_dto

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
