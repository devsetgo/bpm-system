from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="MultiFormDeploymentDto")


@attr.s(auto_attribs=True)
class MultiFormDeploymentDto:
    """ """

    tenant_id: Union[Unset, None, str] = UNSET
    deployment_source: Union[Unset, None, str] = UNSET
    deploy_changed_only: Union[Unset, None, bool] = False
    enable_duplicate_filtering: Union[Unset, None, bool] = False
    deployment_name: Union[Unset, None, str] = UNSET
    data: Union[Unset, None, File] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tenant_id = self.tenant_id
        deployment_source = self.deployment_source
        deploy_changed_only = self.deploy_changed_only
        enable_duplicate_filtering = self.enable_duplicate_filtering
        deployment_name = self.deployment_name
        data: Union[Unset, None, FileJsonType] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_tuple() if self.data else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tenant_id is not UNSET:
            field_dict["tenant-id"] = tenant_id
        if deployment_source is not UNSET:
            field_dict["deployment-source"] = deployment_source
        if deploy_changed_only is not UNSET:
            field_dict["deploy-changed-only"] = deploy_changed_only
        if enable_duplicate_filtering is not UNSET:
            field_dict["enable-duplicate-filtering"] = enable_duplicate_filtering
        if deployment_name is not UNSET:
            field_dict["deployment-name"] = deployment_name
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        tenant_id = self.tenant_id if self.tenant_id is UNSET else (None, str(self.tenant_id), "text/plain")
        deployment_source = (
            self.deployment_source
            if self.deployment_source is UNSET
            else (None, str(self.deployment_source), "text/plain")
        )
        deploy_changed_only = (
            self.deploy_changed_only
            if self.deploy_changed_only is UNSET
            else (None, str(self.deploy_changed_only), "text/plain")
        )
        enable_duplicate_filtering = (
            self.enable_duplicate_filtering
            if self.enable_duplicate_filtering is UNSET
            else (None, str(self.enable_duplicate_filtering), "text/plain")
        )
        deployment_name = (
            self.deployment_name if self.deployment_name is UNSET else (None, str(self.deployment_name), "text/plain")
        )
        data: Union[Unset, None, FileJsonType] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_tuple() if self.data else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
        field_dict.update({})
        if tenant_id is not UNSET:
            field_dict["tenant-id"] = tenant_id
        if deployment_source is not UNSET:
            field_dict["deployment-source"] = deployment_source
        if deploy_changed_only is not UNSET:
            field_dict["deploy-changed-only"] = deploy_changed_only
        if enable_duplicate_filtering is not UNSET:
            field_dict["enable-duplicate-filtering"] = enable_duplicate_filtering
        if deployment_name is not UNSET:
            field_dict["deployment-name"] = deployment_name
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tenant_id = d.pop("tenant-id", UNSET)

        deployment_source = d.pop("deployment-source", UNSET)

        deploy_changed_only = d.pop("deploy-changed-only", UNSET)

        enable_duplicate_filtering = d.pop("enable-duplicate-filtering", UNSET)

        deployment_name = d.pop("deployment-name", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, None, File]
        if _data is None:
            data = None
        elif isinstance(_data, Unset):
            data = UNSET
        else:
            data = File(payload=BytesIO(_data))

        multi_form_deployment_dto = cls(
            tenant_id=tenant_id,
            deployment_source=deployment_source,
            deploy_changed_only=deploy_changed_only,
            enable_duplicate_filtering=enable_duplicate_filtering,
            deployment_name=deployment_name,
            data=data,
        )

        multi_form_deployment_dto.additional_properties = d
        return multi_form_deployment_dto

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
