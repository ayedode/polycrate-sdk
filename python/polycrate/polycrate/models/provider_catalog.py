from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_catalog_bsi_grundschutz_status import (
    ProviderCatalogBsiGrundschutzStatus,
    check_provider_catalog_bsi_grundschutz_status,
)
from ..models.provider_catalog_c5_status import ProviderCatalogC5Status, check_provider_catalog_c5_status
from ..models.provider_catalog_iso_27001_status import (
    ProviderCatalogIso27001Status,
    check_provider_catalog_iso_27001_status,
)
from ..models.provider_catalog_kind import ProviderCatalogKind, check_provider_catalog_kind
from ..models.provider_catalog_scs_iaas_status import (
    ProviderCatalogScsIaasStatus,
    check_provider_catalog_scs_iaas_status,
)
from ..models.provider_catalog_scs_kaas_status import (
    ProviderCatalogScsKaasStatus,
    check_provider_catalog_scs_kaas_status,
)

T = TypeVar("T", bound="ProviderCatalog")


@_attrs_define
class ProviderCatalog:
    """Public catalog slice for authenticated non-staff reads.

    Spec: polycrate spec inspect 941. Omits contacts, evidence, procurement,
    CCM/CSI, and provider URLs. Staff keep ProviderDetailSerializer.

        Attributes:
            id (UUID):
            name (str):
            display_name (None | str): The display name is used to display the object in the UI. It can be different from
                the name.
            slug (None | str): URL-friendly identifier (auto-generated from name if empty)
            legal_name (None | str): Legal company name (e.g. 'Hetzner Online GmbH')
            kind (ProviderCatalogKind): Type of provider (infrastructure, hardware, software)

                * `infrastructure` - Infrastructure
                * `hardware` - Hardware
                * `software` - Software
            active (bool): When false, hidden from new PoP/DataSource/workspace PoP assignments.
            icon_url (str):
            asn (Any): List of AS Numbers, e.g. [{"name": "Default", "value": "AS24940"}]
            iso27001_status (ProviderCatalogIso27001Status): ISO 27001 status for this provider.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            c5_status (ProviderCatalogC5Status): BSI C5 status for this provider.

                * `none` - None
                * `planned` - Planned
                * `typ1` - Type 1
                * `typ2` - Type 2
            bsi_grundschutz_status (ProviderCatalogBsiGrundschutzStatus): BSI IT-Grundschutz status for this provider.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            scs_iaas_status (ProviderCatalogScsIaasStatus): SCS-compatible IaaS status. Public chip only when compatible.

                * `none` - None
                * `compatible` - Compatible
                * `listed_not_certified` - Listed, not certified
            scs_kaas_status (ProviderCatalogScsKaasStatus): SCS-compatible KaaS status. Not the public SCS chip.

                * `none` - None
                * `compatible` - Compatible
                * `listed_not_certified` - Listed, not certified
    """

    id: UUID
    name: str
    display_name: None | str
    slug: None | str
    legal_name: None | str
    kind: ProviderCatalogKind
    active: bool
    icon_url: str
    asn: Any
    iso27001_status: ProviderCatalogIso27001Status
    c5_status: ProviderCatalogC5Status
    bsi_grundschutz_status: ProviderCatalogBsiGrundschutzStatus
    scs_iaas_status: ProviderCatalogScsIaasStatus
    scs_kaas_status: ProviderCatalogScsKaasStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        display_name: None | str
        display_name = self.display_name

        slug: None | str
        slug = self.slug

        legal_name: None | str
        legal_name = self.legal_name

        kind: str = self.kind

        active = self.active

        icon_url = self.icon_url

        asn = self.asn

        iso27001_status: str = self.iso27001_status

        c5_status: str = self.c5_status

        bsi_grundschutz_status: str = self.bsi_grundschutz_status

        scs_iaas_status: str = self.scs_iaas_status

        scs_kaas_status: str = self.scs_kaas_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "slug": slug,
                "legal_name": legal_name,
                "kind": kind,
                "active": active,
                "icon_url": icon_url,
                "asn": asn,
                "iso27001_status": iso27001_status,
                "c5_status": c5_status,
                "bsi_grundschutz_status": bsi_grundschutz_status,
                "scs_iaas_status": scs_iaas_status,
                "scs_kaas_status": scs_kaas_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_legal_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        legal_name = _parse_legal_name(d.pop("legal_name"))

        kind = check_provider_catalog_kind(d.pop("kind"))

        active = d.pop("active")

        icon_url = d.pop("icon_url")

        asn = d.pop("asn")

        iso27001_status = check_provider_catalog_iso_27001_status(d.pop("iso27001_status"))

        c5_status = check_provider_catalog_c5_status(d.pop("c5_status"))

        bsi_grundschutz_status = check_provider_catalog_bsi_grundschutz_status(d.pop("bsi_grundschutz_status"))

        scs_iaas_status = check_provider_catalog_scs_iaas_status(d.pop("scs_iaas_status"))

        scs_kaas_status = check_provider_catalog_scs_kaas_status(d.pop("scs_kaas_status"))

        provider_catalog = cls(
            id=id,
            name=name,
            display_name=display_name,
            slug=slug,
            legal_name=legal_name,
            kind=kind,
            active=active,
            icon_url=icon_url,
            asn=asn,
            iso27001_status=iso27001_status,
            c5_status=c5_status,
            bsi_grundschutz_status=bsi_grundschutz_status,
            scs_iaas_status=scs_iaas_status,
            scs_kaas_status=scs_kaas_status,
        )

        provider_catalog.additional_properties = d
        return provider_catalog

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
