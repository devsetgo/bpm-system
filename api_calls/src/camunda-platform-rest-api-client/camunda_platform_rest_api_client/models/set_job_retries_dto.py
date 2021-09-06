from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.job_query_dto import JobQueryDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetJobRetriesDto")


@attr.s(auto_attribs=True)
class SetJobRetriesDto:
    """Defines the number of retries for a selection of jobs.
    Please note that if both jobIds and jobQuery are provided,
    then retries will be set on the union of these sets."""

    job_ids: Union[Unset, None, List[str]] = UNSET
    job_query: Union[Unset, JobQueryDto] = UNSET
    retries: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.job_ids, Unset):
            if self.job_ids is None:
                job_ids = None
            else:
                job_ids = self.job_ids

        job_query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_query, Unset):
            job_query = self.job_query.to_dict()

        retries = self.retries

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_ids is not UNSET:
            field_dict["jobIds"] = job_ids
        if job_query is not UNSET:
            field_dict["jobQuery"] = job_query
        if retries is not UNSET:
            field_dict["retries"] = retries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_ids = cast(List[str], d.pop("jobIds", UNSET))

        _job_query = d.pop("jobQuery", UNSET)
        job_query: Union[Unset, JobQueryDto]
        if isinstance(_job_query, Unset):
            job_query = UNSET
        else:
            job_query = JobQueryDto.from_dict(_job_query)

        retries = d.pop("retries", UNSET)

        set_job_retries_dto = cls(
            job_ids=job_ids,
            job_query=job_query,
            retries=retries,
        )

        set_job_retries_dto.additional_properties = d
        return set_job_retries_dto

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
