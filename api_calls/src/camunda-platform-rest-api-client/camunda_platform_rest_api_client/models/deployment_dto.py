import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.atom_link import AtomLink
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentDto")


@attr.s(auto_attribs=True)
class DeploymentDto:
    """ """

    links: Union[Unset, None, List[AtomLink]] = UNSET
    id: Union[Unset, None, str] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    deployment_time: Union[Unset, None, datetime.datetime] = UNSET
    source: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
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
        tenant_id = self.tenant_id
        deployment_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.deployment_time, Unset):
            deployment_time = self.deployment_time.isoformat() if self.deployment_time else None

        source = self.source
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if deployment_time is not UNSET:
            field_dict["deploymentTime"] = deployment_time
        if source is not UNSET:
            field_dict["source"] = source
        if name is not UNSET:
            field_dict["name"] = name

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

        tenant_id = d.pop("tenantId", UNSET)

        _deployment_time = d.pop("deploymentTime", UNSET)
        deployment_time: Union[Unset, None, datetime.datetime]
        if _deployment_time is None:
            deployment_time = None
        elif isinstance(_deployment_time, Unset):
            deployment_time = UNSET
        else:
            deployment_time = isoparse(_deployment_time)

        source = d.pop("source", UNSET)

        name = d.pop("name", UNSET)

        deployment_dto = cls(
            links=links,
            id=id,
            tenant_id=tenant_id,
            deployment_time=deployment_time,
            source=source,
            name=name,
        )

        deployment_dto.additional_properties = d
        return deployment_dto

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
