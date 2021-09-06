from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.atom_link import AtomLink
from ..models.process_instance_with_variables_dto_variables import ProcessInstanceWithVariablesDtoVariables
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessInstanceWithVariablesDto")


@attr.s(auto_attribs=True)
class ProcessInstanceWithVariablesDto:
    """ """

    links: Union[Unset, None, List[AtomLink]] = UNSET
    id: Union[Unset, None, str] = UNSET
    definition_id: Union[Unset, None, str] = UNSET
    business_key: Union[Unset, None, str] = UNSET
    case_instance_id: Union[Unset, None, str] = UNSET
    ended: Union[Unset, None, bool] = UNSET
    suspended: Union[Unset, None, bool] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    variables: Union[Unset, None, ProcessInstanceWithVariablesDtoVariables] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            if self.links is None:
                links = None
            else:
                links = []
                for links_item_data in self.links:
                    links_item = links_item_data.to_dict()

                    links.append(links_item)

        id = self.id
        definition_id = self.definition_id
        business_key = self.business_key
        case_instance_id = self.case_instance_id
        ended = self.ended
        suspended = self.suspended
        tenant_id = self.tenant_id
        variables: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict() if self.variables else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if id is not UNSET:
            field_dict["id"] = id
        if definition_id is not UNSET:
            field_dict["definitionId"] = definition_id
        if business_key is not UNSET:
            field_dict["businessKey"] = business_key
        if case_instance_id is not UNSET:
            field_dict["caseInstanceId"] = case_instance_id
        if ended is not UNSET:
            field_dict["ended"] = ended
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = AtomLink.from_dict(links_item_data)

            links.append(links_item)

        id = d.pop("id", UNSET)

        definition_id = d.pop("definitionId", UNSET)

        business_key = d.pop("businessKey", UNSET)

        case_instance_id = d.pop("caseInstanceId", UNSET)

        ended = d.pop("ended", UNSET)

        suspended = d.pop("suspended", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, None, ProcessInstanceWithVariablesDtoVariables]
        if _variables is None:
            variables = None
        elif isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = ProcessInstanceWithVariablesDtoVariables.from_dict(_variables)

        process_instance_with_variables_dto = cls(
            links=links,
            id=id,
            definition_id=definition_id,
            business_key=business_key,
            case_instance_id=case_instance_id,
            ended=ended,
            suspended=suspended,
            tenant_id=tenant_id,
            variables=variables,
        )

        process_instance_with_variables_dto.additional_properties = d
        return process_instance_with_variables_dto

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
