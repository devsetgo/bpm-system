from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionDto")


@attr.s(auto_attribs=True)
class ExecutionDto:
    """ """

    id: Union[Unset, None, str] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    ended: Union[Unset, None, bool] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        process_instance_id = self.process_instance_id
        ended = self.ended
        tenant_id = self.tenant_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if ended is not UNSET:
            field_dict["ended"] = ended
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        ended = d.pop("ended", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        execution_dto = cls(
            id=id,
            process_instance_id=process_instance_id,
            ended=ended,
            tenant_id=tenant_id,
        )

        execution_dto.additional_properties = d
        return execution_dto

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
