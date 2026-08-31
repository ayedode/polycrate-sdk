from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_ipaddresses_create_annotations_error_component import (
        ApiV1IpaddressesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_archived_at_error_component import (
        ApiV1IpaddressesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_archived_error_component import ApiV1IpaddressesCreateArchivedErrorComponent
    from ..models.api_v1_ipaddresses_create_archived_reason_error_component import (
        ApiV1IpaddressesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_credential_id_error_component import (
        ApiV1IpaddressesCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_criticality_error_component import (
        ApiV1IpaddressesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_debug_mode_error_component import (
        ApiV1IpaddressesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_display_name_error_component import (
        ApiV1IpaddressesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_ip_address_error_component import (
        ApiV1IpaddressesCreateIpAddressErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_kind_error_component import ApiV1IpaddressesCreateKindErrorComponent
    from ..models.api_v1_ipaddresses_create_labels_error_component import ApiV1IpaddressesCreateLabelsErrorComponent
    from ..models.api_v1_ipaddresses_create_name_error_component import ApiV1IpaddressesCreateNameErrorComponent
    from ..models.api_v1_ipaddresses_create_non_field_errors_error_component import (
        ApiV1IpaddressesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_organization_id_error_component import (
        ApiV1IpaddressesCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_platform_service_error_component import (
        ApiV1IpaddressesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_prefix_id_error_component import (
        ApiV1IpaddressesCreatePrefixIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_provider_error_component import ApiV1IpaddressesCreateProviderErrorComponent
    from ..models.api_v1_ipaddresses_create_provider_id_error_component import (
        ApiV1IpaddressesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_provider_reference_error_component import (
        ApiV1IpaddressesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_reconciliation_enabled_error_component import (
        ApiV1IpaddressesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_sla_availability_error_component import (
        ApiV1IpaddressesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_sla_target_error_component import (
        ApiV1IpaddressesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_slo_availability_error_component import (
        ApiV1IpaddressesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_slo_target_error_component import (
        ApiV1IpaddressesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_target_availability_error_component import (
        ApiV1IpaddressesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_tolerations_error_component import (
        ApiV1IpaddressesCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_ipaddresses_create_workspace_id_error_component import (
        ApiV1IpaddressesCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1IpaddressesCreateValidationError")


@_attrs_define
class ApiV1IpaddressesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1IpaddressesCreateAnnotationsErrorComponent | ApiV1IpaddressesCreateArchivedAtErrorComponent |
            ApiV1IpaddressesCreateArchivedErrorComponent | ApiV1IpaddressesCreateArchivedReasonErrorComponent |
            ApiV1IpaddressesCreateCredentialIdErrorComponent | ApiV1IpaddressesCreateCriticalityErrorComponent |
            ApiV1IpaddressesCreateDebugModeErrorComponent | ApiV1IpaddressesCreateDisplayNameErrorComponent |
            ApiV1IpaddressesCreateIpAddressErrorComponent | ApiV1IpaddressesCreateKindErrorComponent |
            ApiV1IpaddressesCreateLabelsErrorComponent | ApiV1IpaddressesCreateNameErrorComponent |
            ApiV1IpaddressesCreateNonFieldErrorsErrorComponent | ApiV1IpaddressesCreateOrganizationIdErrorComponent |
            ApiV1IpaddressesCreatePlatformServiceErrorComponent | ApiV1IpaddressesCreatePrefixIdErrorComponent |
            ApiV1IpaddressesCreateProviderErrorComponent | ApiV1IpaddressesCreateProviderIdErrorComponent |
            ApiV1IpaddressesCreateProviderReferenceErrorComponent |
            ApiV1IpaddressesCreateReconciliationEnabledErrorComponent | ApiV1IpaddressesCreateSlaAvailabilityErrorComponent
            | ApiV1IpaddressesCreateSlaTargetErrorComponent | ApiV1IpaddressesCreateSloAvailabilityErrorComponent |
            ApiV1IpaddressesCreateSloTargetErrorComponent | ApiV1IpaddressesCreateTargetAvailabilityErrorComponent |
            ApiV1IpaddressesCreateTolerationsErrorComponent | ApiV1IpaddressesCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1IpaddressesCreateAnnotationsErrorComponent
        | ApiV1IpaddressesCreateArchivedAtErrorComponent
        | ApiV1IpaddressesCreateArchivedErrorComponent
        | ApiV1IpaddressesCreateArchivedReasonErrorComponent
        | ApiV1IpaddressesCreateCredentialIdErrorComponent
        | ApiV1IpaddressesCreateCriticalityErrorComponent
        | ApiV1IpaddressesCreateDebugModeErrorComponent
        | ApiV1IpaddressesCreateDisplayNameErrorComponent
        | ApiV1IpaddressesCreateIpAddressErrorComponent
        | ApiV1IpaddressesCreateKindErrorComponent
        | ApiV1IpaddressesCreateLabelsErrorComponent
        | ApiV1IpaddressesCreateNameErrorComponent
        | ApiV1IpaddressesCreateNonFieldErrorsErrorComponent
        | ApiV1IpaddressesCreateOrganizationIdErrorComponent
        | ApiV1IpaddressesCreatePlatformServiceErrorComponent
        | ApiV1IpaddressesCreatePrefixIdErrorComponent
        | ApiV1IpaddressesCreateProviderErrorComponent
        | ApiV1IpaddressesCreateProviderIdErrorComponent
        | ApiV1IpaddressesCreateProviderReferenceErrorComponent
        | ApiV1IpaddressesCreateReconciliationEnabledErrorComponent
        | ApiV1IpaddressesCreateSlaAvailabilityErrorComponent
        | ApiV1IpaddressesCreateSlaTargetErrorComponent
        | ApiV1IpaddressesCreateSloAvailabilityErrorComponent
        | ApiV1IpaddressesCreateSloTargetErrorComponent
        | ApiV1IpaddressesCreateTargetAvailabilityErrorComponent
        | ApiV1IpaddressesCreateTolerationsErrorComponent
        | ApiV1IpaddressesCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_ipaddresses_create_annotations_error_component import (
            ApiV1IpaddressesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_archived_at_error_component import (
            ApiV1IpaddressesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_archived_error_component import (
            ApiV1IpaddressesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_archived_reason_error_component import (
            ApiV1IpaddressesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_credential_id_error_component import (
            ApiV1IpaddressesCreateCredentialIdErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_criticality_error_component import (
            ApiV1IpaddressesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_debug_mode_error_component import (
            ApiV1IpaddressesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_display_name_error_component import (
            ApiV1IpaddressesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_kind_error_component import ApiV1IpaddressesCreateKindErrorComponent
        from ..models.api_v1_ipaddresses_create_labels_error_component import ApiV1IpaddressesCreateLabelsErrorComponent
        from ..models.api_v1_ipaddresses_create_name_error_component import ApiV1IpaddressesCreateNameErrorComponent
        from ..models.api_v1_ipaddresses_create_non_field_errors_error_component import (
            ApiV1IpaddressesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_organization_id_error_component import (
            ApiV1IpaddressesCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_platform_service_error_component import (
            ApiV1IpaddressesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_prefix_id_error_component import (
            ApiV1IpaddressesCreatePrefixIdErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_provider_error_component import (
            ApiV1IpaddressesCreateProviderErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_provider_id_error_component import (
            ApiV1IpaddressesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_provider_reference_error_component import (
            ApiV1IpaddressesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_reconciliation_enabled_error_component import (
            ApiV1IpaddressesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_sla_availability_error_component import (
            ApiV1IpaddressesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_sla_target_error_component import (
            ApiV1IpaddressesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_slo_availability_error_component import (
            ApiV1IpaddressesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_slo_target_error_component import (
            ApiV1IpaddressesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_target_availability_error_component import (
            ApiV1IpaddressesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_tolerations_error_component import (
            ApiV1IpaddressesCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_workspace_id_error_component import (
            ApiV1IpaddressesCreateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1IpaddressesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesCreatePrefixIdErrorComponent):
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
        from ..models.api_v1_ipaddresses_create_annotations_error_component import (
            ApiV1IpaddressesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_archived_at_error_component import (
            ApiV1IpaddressesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_archived_error_component import (
            ApiV1IpaddressesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_archived_reason_error_component import (
            ApiV1IpaddressesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_credential_id_error_component import (
            ApiV1IpaddressesCreateCredentialIdErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_criticality_error_component import (
            ApiV1IpaddressesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_debug_mode_error_component import (
            ApiV1IpaddressesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_display_name_error_component import (
            ApiV1IpaddressesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_ip_address_error_component import (
            ApiV1IpaddressesCreateIpAddressErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_kind_error_component import ApiV1IpaddressesCreateKindErrorComponent
        from ..models.api_v1_ipaddresses_create_labels_error_component import ApiV1IpaddressesCreateLabelsErrorComponent
        from ..models.api_v1_ipaddresses_create_name_error_component import ApiV1IpaddressesCreateNameErrorComponent
        from ..models.api_v1_ipaddresses_create_non_field_errors_error_component import (
            ApiV1IpaddressesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_organization_id_error_component import (
            ApiV1IpaddressesCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_platform_service_error_component import (
            ApiV1IpaddressesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_prefix_id_error_component import (
            ApiV1IpaddressesCreatePrefixIdErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_provider_error_component import (
            ApiV1IpaddressesCreateProviderErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_provider_id_error_component import (
            ApiV1IpaddressesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_provider_reference_error_component import (
            ApiV1IpaddressesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_reconciliation_enabled_error_component import (
            ApiV1IpaddressesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_sla_availability_error_component import (
            ApiV1IpaddressesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_sla_target_error_component import (
            ApiV1IpaddressesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_slo_availability_error_component import (
            ApiV1IpaddressesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_slo_target_error_component import (
            ApiV1IpaddressesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_target_availability_error_component import (
            ApiV1IpaddressesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_tolerations_error_component import (
            ApiV1IpaddressesCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_ipaddresses_create_workspace_id_error_component import (
            ApiV1IpaddressesCreateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1IpaddressesCreateAnnotationsErrorComponent
                | ApiV1IpaddressesCreateArchivedAtErrorComponent
                | ApiV1IpaddressesCreateArchivedErrorComponent
                | ApiV1IpaddressesCreateArchivedReasonErrorComponent
                | ApiV1IpaddressesCreateCredentialIdErrorComponent
                | ApiV1IpaddressesCreateCriticalityErrorComponent
                | ApiV1IpaddressesCreateDebugModeErrorComponent
                | ApiV1IpaddressesCreateDisplayNameErrorComponent
                | ApiV1IpaddressesCreateIpAddressErrorComponent
                | ApiV1IpaddressesCreateKindErrorComponent
                | ApiV1IpaddressesCreateLabelsErrorComponent
                | ApiV1IpaddressesCreateNameErrorComponent
                | ApiV1IpaddressesCreateNonFieldErrorsErrorComponent
                | ApiV1IpaddressesCreateOrganizationIdErrorComponent
                | ApiV1IpaddressesCreatePlatformServiceErrorComponent
                | ApiV1IpaddressesCreatePrefixIdErrorComponent
                | ApiV1IpaddressesCreateProviderErrorComponent
                | ApiV1IpaddressesCreateProviderIdErrorComponent
                | ApiV1IpaddressesCreateProviderReferenceErrorComponent
                | ApiV1IpaddressesCreateReconciliationEnabledErrorComponent
                | ApiV1IpaddressesCreateSlaAvailabilityErrorComponent
                | ApiV1IpaddressesCreateSlaTargetErrorComponent
                | ApiV1IpaddressesCreateSloAvailabilityErrorComponent
                | ApiV1IpaddressesCreateSloTargetErrorComponent
                | ApiV1IpaddressesCreateTargetAvailabilityErrorComponent
                | ApiV1IpaddressesCreateTolerationsErrorComponent
                | ApiV1IpaddressesCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_0 = (
                        ApiV1IpaddressesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_1 = (
                        ApiV1IpaddressesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_2 = (
                        ApiV1IpaddressesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_3 = (
                        ApiV1IpaddressesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_4 = (
                        ApiV1IpaddressesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_5 = (
                        ApiV1IpaddressesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_6 = (
                        ApiV1IpaddressesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_7 = (
                        ApiV1IpaddressesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_8 = (
                        ApiV1IpaddressesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_9 = (
                        ApiV1IpaddressesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_10 = (
                        ApiV1IpaddressesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_11 = (
                        ApiV1IpaddressesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_12 = (
                        ApiV1IpaddressesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_13 = (
                        ApiV1IpaddressesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_14 = (
                        ApiV1IpaddressesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_15 = (
                        ApiV1IpaddressesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_16 = (
                        ApiV1IpaddressesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_17 = (
                        ApiV1IpaddressesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_18 = (
                        ApiV1IpaddressesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_19 = (
                        ApiV1IpaddressesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_20 = (
                        ApiV1IpaddressesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_21 = (
                        ApiV1IpaddressesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_22 = (
                        ApiV1IpaddressesCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_23 = (
                        ApiV1IpaddressesCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_24 = (
                        ApiV1IpaddressesCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_create_error_type_25 = (
                        ApiV1IpaddressesCreatePrefixIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_ipaddresses_create_error_type_26 = (
                    ApiV1IpaddressesCreateIpAddressErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_ipaddresses_create_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_ipaddresses_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_ipaddresses_create_validation_error.additional_properties = d
        return api_v1_ipaddresses_create_validation_error

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
