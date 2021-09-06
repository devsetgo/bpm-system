from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtendLockOnExternalTaskDto")


@attr.s(auto_attribs=True)
class ExtendLockOnExternalTaskDto:
    """ """

    worker_id: Union[Unset, str] = UNSET
    new_duration: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        worker_id = self.worker_id
        new_duration = self.new_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if worker_id is not UNSET:
            field_dict["workerId"] = worker_id
        if new_duration is not UNSET:
            field_dict["newDuration"] = new_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        worker_id = d.pop("workerId", UNSET)

        new_duration = d.pop("newDuration", UNSET)

        extend_lock_on_external_task_dto = cls(
            worker_id=worker_id,
            new_duration=new_duration,
        )

        extend_lock_on_external_task_dto.additional_properties = d
        return extend_lock_on_external_task_dto

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
