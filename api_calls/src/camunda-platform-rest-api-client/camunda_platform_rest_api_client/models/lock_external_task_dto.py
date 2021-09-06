from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LockExternalTaskDto")


@attr.s(auto_attribs=True)
class LockExternalTaskDto:
    """ """

    worker_id: Union[Unset, str] = UNSET
    lock_duration: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        worker_id = self.worker_id
        lock_duration = self.lock_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if worker_id is not UNSET:
            field_dict["workerId"] = worker_id
        if lock_duration is not UNSET:
            field_dict["lockDuration"] = lock_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        worker_id = d.pop("workerId", UNSET)

        lock_duration = d.pop("lockDuration", UNSET)

        lock_external_task_dto = cls(
            worker_id=worker_id,
            lock_duration=lock_duration,
        )

        lock_external_task_dto.additional_properties = d
        return lock_external_task_dto

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
