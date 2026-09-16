from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_ipaddresses_archive_create_annotations_error_component import (
        ApiV1IpaddressesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_archived_at_error_component import (
        ApiV1IpaddressesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_archived_error_component import (
        ApiV1IpaddressesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_archived_reason_error_component import (
        ApiV1IpaddressesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_credential_id_error_component import (
        ApiV1IpaddressesArchiveCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_criticality_error_component import (
        ApiV1IpaddressesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_debug_mode_error_component import (
        ApiV1IpaddressesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_display_name_error_component import (
        ApiV1IpaddressesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_ip_address_error_component import (
        ApiV1IpaddressesArchiveCreateIpAddressErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_kind_error_component import (
        ApiV1IpaddressesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_labels_error_component import (
        ApiV1IpaddressesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_name_error_component import (
        ApiV1IpaddressesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_non_field_errors_error_component import (
        ApiV1IpaddressesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_organization_id_error_component import (
        ApiV1IpaddressesArchiveCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_platform_service_error_component import (
        ApiV1IpaddressesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_prefix_id_error_component import (
        ApiV1IpaddressesArchiveCreatePrefixIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_provider_error_component import (
        ApiV1IpaddressesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_provider_id_error_component import (
        ApiV1IpaddressesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_provider_reference_error_component import (
        ApiV1IpaddressesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_reconciliation_enabled_error_component import (
        ApiV1IpaddressesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_sla_availability_error_component import (
        ApiV1IpaddressesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_sla_target_error_component import (
        ApiV1IpaddressesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_slo_availability_error_component import (
        ApiV1IpaddressesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_slo_target_error_component import (
        ApiV1IpaddressesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_target_availability_error_component import (
        ApiV1IpaddressesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_tolerations_error_component import (
        ApiV1IpaddressesArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_ipaddresses_archive_create_workspace_id_error_component import (
        ApiV1IpaddressesArchiveCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1IpaddressesArchiveCreateValidationError")


@_attrs_define
class ApiV1IpaddressesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1IpaddressesArchiveCreateAnnotationsErrorComponent |
            ApiV1IpaddressesArchiveCreateArchivedAtErrorComponent | ApiV1IpaddressesArchiveCreateArchivedErrorComponent |
            ApiV1IpaddressesArchiveCreateArchivedReasonErrorComponent |
            ApiV1IpaddressesArchiveCreateCredentialIdErrorComponent | ApiV1IpaddressesArchiveCreateCriticalityErrorComponent
            | ApiV1IpaddressesArchiveCreateDebugModeErrorComponent | ApiV1IpaddressesArchiveCreateDisplayNameErrorComponent
            | ApiV1IpaddressesArchiveCreateIpAddressErrorComponent | ApiV1IpaddressesArchiveCreateKindErrorComponent |
            ApiV1IpaddressesArchiveCreateLabelsErrorComponent | ApiV1IpaddressesArchiveCreateNameErrorComponent |
            ApiV1IpaddressesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1IpaddressesArchiveCreateOrganizationIdErrorComponent |
            ApiV1IpaddressesArchiveCreatePlatformServiceErrorComponent | ApiV1IpaddressesArchiveCreatePrefixIdErrorComponent
            | ApiV1IpaddressesArchiveCreateProviderErrorComponent | ApiV1IpaddressesArchiveCreateProviderIdErrorComponent |
            ApiV1IpaddressesArchiveCreateProviderReferenceErrorComponent |
            ApiV1IpaddressesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1IpaddressesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1IpaddressesArchiveCreateSlaTargetErrorComponent |
            ApiV1IpaddressesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1IpaddressesArchiveCreateSloTargetErrorComponent |
            ApiV1IpaddressesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1IpaddressesArchiveCreateTolerationsErrorComponent |
            ApiV1IpaddressesArchiveCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1IpaddressesArchiveCreateAnnotationsErrorComponent
        | ApiV1IpaddressesArchiveCreateArchivedAtErrorComponent
        | ApiV1IpaddressesArchiveCreateArchivedErrorComponent
        | ApiV1IpaddressesArchiveCreateArchivedReasonErrorComponent
        | ApiV1IpaddressesArchiveCreateCredentialIdErrorComponent
        | ApiV1IpaddressesArchiveCreateCriticalityErrorComponent
        | ApiV1IpaddressesArchiveCreateDebugModeErrorComponent
        | ApiV1IpaddressesArchiveCreateDisplayNameErrorComponent
        | ApiV1IpaddressesArchiveCreateIpAddressErrorComponent
        | ApiV1IpaddressesArchiveCreateKindErrorComponent
        | ApiV1IpaddressesArchiveCreateLabelsErrorComponent
        | ApiV1IpaddressesArchiveCreateNameErrorComponent
        | ApiV1IpaddressesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1IpaddressesArchiveCreateOrganizationIdErrorComponent
        | ApiV1IpaddressesArchiveCreatePlatformServiceErrorComponent
        | ApiV1IpaddressesArchiveCreatePrefixIdErrorComponent
        | ApiV1IpaddressesArchiveCreateProviderErrorComponent
        | ApiV1IpaddressesArchiveCreateProviderIdErrorComponent
        | ApiV1IpaddressesArchiveCreateProviderReferenceErrorComponent
        | ApiV1IpaddressesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1IpaddressesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1IpaddressesArchiveCreateSlaTargetErrorComponent
        | ApiV1IpaddressesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1IpaddressesArchiveCreateSloTargetErrorComponent
        | ApiV1IpaddressesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1IpaddressesArchiveCreateTolerationsErrorComponent
        | ApiV1IpaddressesArchiveCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_ipaddresses_archive_create_annotations_error_component import (
            ApiV1IpaddressesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_archived_at_error_component import (
            ApiV1IpaddressesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_archived_error_component import (
            ApiV1IpaddressesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_archived_reason_error_component import (
            ApiV1IpaddressesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_credential_id_error_component import (
            ApiV1IpaddressesArchiveCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_criticality_error_component import (
            ApiV1IpaddressesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_debug_mode_error_component import (
            ApiV1IpaddressesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_display_name_error_component import (
            ApiV1IpaddressesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_kind_error_component import (
            ApiV1IpaddressesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_labels_error_component import (
            ApiV1IpaddressesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_name_error_component import (
            ApiV1IpaddressesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_non_field_errors_error_component import (
            ApiV1IpaddressesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_organization_id_error_component import (
            ApiV1IpaddressesArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_platform_service_error_component import (
            ApiV1IpaddressesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_prefix_id_error_component import (
            ApiV1IpaddressesArchiveCreatePrefixIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_provider_error_component import (
            ApiV1IpaddressesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_provider_id_error_component import (
            ApiV1IpaddressesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_provider_reference_error_component import (
            ApiV1IpaddressesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_reconciliation_enabled_error_component import (
            ApiV1IpaddressesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_sla_availability_error_component import (
            ApiV1IpaddressesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_sla_target_error_component import (
            ApiV1IpaddressesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_slo_availability_error_component import (
            ApiV1IpaddressesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_slo_target_error_component import (
            ApiV1IpaddressesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_target_availability_error_component import (
            ApiV1IpaddressesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_tolerations_error_component import (
            ApiV1IpaddressesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_workspace_id_error_component import (
            ApiV1IpaddressesArchiveCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesArchiveCreatePrefixIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_ipaddresses_archive_create_annotations_error_component import (
            ApiV1IpaddressesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_archived_at_error_component import (
            ApiV1IpaddressesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_archived_error_component import (
            ApiV1IpaddressesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_archived_reason_error_component import (
            ApiV1IpaddressesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_credential_id_error_component import (
            ApiV1IpaddressesArchiveCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_criticality_error_component import (
            ApiV1IpaddressesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_debug_mode_error_component import (
            ApiV1IpaddressesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_display_name_error_component import (
            ApiV1IpaddressesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_ip_address_error_component import (
            ApiV1IpaddressesArchiveCreateIpAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_kind_error_component import (
            ApiV1IpaddressesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_labels_error_component import (
            ApiV1IpaddressesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_name_error_component import (
            ApiV1IpaddressesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_non_field_errors_error_component import (
            ApiV1IpaddressesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_organization_id_error_component import (
            ApiV1IpaddressesArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_platform_service_error_component import (
            ApiV1IpaddressesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_prefix_id_error_component import (
            ApiV1IpaddressesArchiveCreatePrefixIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_provider_error_component import (
            ApiV1IpaddressesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_provider_id_error_component import (
            ApiV1IpaddressesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_provider_reference_error_component import (
            ApiV1IpaddressesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_reconciliation_enabled_error_component import (
            ApiV1IpaddressesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_sla_availability_error_component import (
            ApiV1IpaddressesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_sla_target_error_component import (
            ApiV1IpaddressesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_slo_availability_error_component import (
            ApiV1IpaddressesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_slo_target_error_component import (
            ApiV1IpaddressesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_target_availability_error_component import (
            ApiV1IpaddressesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_tolerations_error_component import (
            ApiV1IpaddressesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_archive_create_workspace_id_error_component import (
            ApiV1IpaddressesArchiveCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1IpaddressesArchiveCreateAnnotationsErrorComponent
                | ApiV1IpaddressesArchiveCreateArchivedAtErrorComponent
                | ApiV1IpaddressesArchiveCreateArchivedErrorComponent
                | ApiV1IpaddressesArchiveCreateArchivedReasonErrorComponent
                | ApiV1IpaddressesArchiveCreateCredentialIdErrorComponent
                | ApiV1IpaddressesArchiveCreateCriticalityErrorComponent
                | ApiV1IpaddressesArchiveCreateDebugModeErrorComponent
                | ApiV1IpaddressesArchiveCreateDisplayNameErrorComponent
                | ApiV1IpaddressesArchiveCreateIpAddressErrorComponent
                | ApiV1IpaddressesArchiveCreateKindErrorComponent
                | ApiV1IpaddressesArchiveCreateLabelsErrorComponent
                | ApiV1IpaddressesArchiveCreateNameErrorComponent
                | ApiV1IpaddressesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1IpaddressesArchiveCreateOrganizationIdErrorComponent
                | ApiV1IpaddressesArchiveCreatePlatformServiceErrorComponent
                | ApiV1IpaddressesArchiveCreatePrefixIdErrorComponent
                | ApiV1IpaddressesArchiveCreateProviderErrorComponent
                | ApiV1IpaddressesArchiveCreateProviderIdErrorComponent
                | ApiV1IpaddressesArchiveCreateProviderReferenceErrorComponent
                | ApiV1IpaddressesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1IpaddressesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1IpaddressesArchiveCreateSlaTargetErrorComponent
                | ApiV1IpaddressesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1IpaddressesArchiveCreateSloTargetErrorComponent
                | ApiV1IpaddressesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1IpaddressesArchiveCreateTolerationsErrorComponent
                | ApiV1IpaddressesArchiveCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_0 = (
                        ApiV1IpaddressesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_1 = (
                        ApiV1IpaddressesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_2 = (
                        ApiV1IpaddressesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_3 = (
                        ApiV1IpaddressesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_4 = (
                        ApiV1IpaddressesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_5 = (
                        ApiV1IpaddressesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_6 = (
                        ApiV1IpaddressesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_7 = (
                        ApiV1IpaddressesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_8 = (
                        ApiV1IpaddressesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_9 = (
                        ApiV1IpaddressesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_10 = (
                        ApiV1IpaddressesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_11 = (
                        ApiV1IpaddressesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_12 = (
                        ApiV1IpaddressesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_13 = (
                        ApiV1IpaddressesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_14 = (
                        ApiV1IpaddressesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_15 = (
                        ApiV1IpaddressesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_16 = (
                        ApiV1IpaddressesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_17 = (
                        ApiV1IpaddressesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_18 = (
                        ApiV1IpaddressesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_19 = (
                        ApiV1IpaddressesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_20 = (
                        ApiV1IpaddressesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_21 = (
                        ApiV1IpaddressesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_22 = (
                        ApiV1IpaddressesArchiveCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_23 = (
                        ApiV1IpaddressesArchiveCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_24 = (
                        ApiV1IpaddressesArchiveCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_archive_create_error_type_25 = (
                        ApiV1IpaddressesArchiveCreatePrefixIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_ipaddresses_archive_create_error_type_26 = (
                    ApiV1IpaddressesArchiveCreateIpAddressErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_ipaddresses_archive_create_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_ipaddresses_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_ipaddresses_archive_create_validation_error.additional_properties = d
        return api_v1_ipaddresses_archive_create_validation_error

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
