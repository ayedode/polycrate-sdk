from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_ipaddresses_partial_update_annotations_error_component import (
        ApiV1IpaddressesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_archived_at_error_component import (
        ApiV1IpaddressesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_archived_error_component import (
        ApiV1IpaddressesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_archived_reason_error_component import (
        ApiV1IpaddressesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_credential_id_error_component import (
        ApiV1IpaddressesPartialUpdateCredentialIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_criticality_error_component import (
        ApiV1IpaddressesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_debug_mode_error_component import (
        ApiV1IpaddressesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_display_name_error_component import (
        ApiV1IpaddressesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_ip_address_error_component import (
        ApiV1IpaddressesPartialUpdateIpAddressErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_kind_error_component import (
        ApiV1IpaddressesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_labels_error_component import (
        ApiV1IpaddressesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_name_error_component import (
        ApiV1IpaddressesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_non_field_errors_error_component import (
        ApiV1IpaddressesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_organization_id_error_component import (
        ApiV1IpaddressesPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_platform_service_error_component import (
        ApiV1IpaddressesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_prefix_id_error_component import (
        ApiV1IpaddressesPartialUpdatePrefixIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_provider_error_component import (
        ApiV1IpaddressesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_provider_id_error_component import (
        ApiV1IpaddressesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_provider_reference_error_component import (
        ApiV1IpaddressesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_reconciliation_enabled_error_component import (
        ApiV1IpaddressesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_sla_availability_error_component import (
        ApiV1IpaddressesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_sla_target_error_component import (
        ApiV1IpaddressesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_slo_availability_error_component import (
        ApiV1IpaddressesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_slo_target_error_component import (
        ApiV1IpaddressesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_target_availability_error_component import (
        ApiV1IpaddressesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_tolerations_error_component import (
        ApiV1IpaddressesPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_ipaddresses_partial_update_workspace_id_error_component import (
        ApiV1IpaddressesPartialUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1IpaddressesPartialUpdateValidationError")


@_attrs_define
class ApiV1IpaddressesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1IpaddressesPartialUpdateAnnotationsErrorComponent |
            ApiV1IpaddressesPartialUpdateArchivedAtErrorComponent | ApiV1IpaddressesPartialUpdateArchivedErrorComponent |
            ApiV1IpaddressesPartialUpdateArchivedReasonErrorComponent |
            ApiV1IpaddressesPartialUpdateCredentialIdErrorComponent | ApiV1IpaddressesPartialUpdateCriticalityErrorComponent
            | ApiV1IpaddressesPartialUpdateDebugModeErrorComponent | ApiV1IpaddressesPartialUpdateDisplayNameErrorComponent
            | ApiV1IpaddressesPartialUpdateIpAddressErrorComponent | ApiV1IpaddressesPartialUpdateKindErrorComponent |
            ApiV1IpaddressesPartialUpdateLabelsErrorComponent | ApiV1IpaddressesPartialUpdateNameErrorComponent |
            ApiV1IpaddressesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1IpaddressesPartialUpdateOrganizationIdErrorComponent |
            ApiV1IpaddressesPartialUpdatePlatformServiceErrorComponent | ApiV1IpaddressesPartialUpdatePrefixIdErrorComponent
            | ApiV1IpaddressesPartialUpdateProviderErrorComponent | ApiV1IpaddressesPartialUpdateProviderIdErrorComponent |
            ApiV1IpaddressesPartialUpdateProviderReferenceErrorComponent |
            ApiV1IpaddressesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1IpaddressesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1IpaddressesPartialUpdateSlaTargetErrorComponent |
            ApiV1IpaddressesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1IpaddressesPartialUpdateSloTargetErrorComponent |
            ApiV1IpaddressesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1IpaddressesPartialUpdateTolerationsErrorComponent |
            ApiV1IpaddressesPartialUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1IpaddressesPartialUpdateAnnotationsErrorComponent
        | ApiV1IpaddressesPartialUpdateArchivedAtErrorComponent
        | ApiV1IpaddressesPartialUpdateArchivedErrorComponent
        | ApiV1IpaddressesPartialUpdateArchivedReasonErrorComponent
        | ApiV1IpaddressesPartialUpdateCredentialIdErrorComponent
        | ApiV1IpaddressesPartialUpdateCriticalityErrorComponent
        | ApiV1IpaddressesPartialUpdateDebugModeErrorComponent
        | ApiV1IpaddressesPartialUpdateDisplayNameErrorComponent
        | ApiV1IpaddressesPartialUpdateIpAddressErrorComponent
        | ApiV1IpaddressesPartialUpdateKindErrorComponent
        | ApiV1IpaddressesPartialUpdateLabelsErrorComponent
        | ApiV1IpaddressesPartialUpdateNameErrorComponent
        | ApiV1IpaddressesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1IpaddressesPartialUpdateOrganizationIdErrorComponent
        | ApiV1IpaddressesPartialUpdatePlatformServiceErrorComponent
        | ApiV1IpaddressesPartialUpdatePrefixIdErrorComponent
        | ApiV1IpaddressesPartialUpdateProviderErrorComponent
        | ApiV1IpaddressesPartialUpdateProviderIdErrorComponent
        | ApiV1IpaddressesPartialUpdateProviderReferenceErrorComponent
        | ApiV1IpaddressesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1IpaddressesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1IpaddressesPartialUpdateSlaTargetErrorComponent
        | ApiV1IpaddressesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1IpaddressesPartialUpdateSloTargetErrorComponent
        | ApiV1IpaddressesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1IpaddressesPartialUpdateTolerationsErrorComponent
        | ApiV1IpaddressesPartialUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_ipaddresses_partial_update_annotations_error_component import (
            ApiV1IpaddressesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_archived_at_error_component import (
            ApiV1IpaddressesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_archived_error_component import (
            ApiV1IpaddressesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_archived_reason_error_component import (
            ApiV1IpaddressesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_credential_id_error_component import (
            ApiV1IpaddressesPartialUpdateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_criticality_error_component import (
            ApiV1IpaddressesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_debug_mode_error_component import (
            ApiV1IpaddressesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_display_name_error_component import (
            ApiV1IpaddressesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_kind_error_component import (
            ApiV1IpaddressesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_labels_error_component import (
            ApiV1IpaddressesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_name_error_component import (
            ApiV1IpaddressesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_non_field_errors_error_component import (
            ApiV1IpaddressesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_organization_id_error_component import (
            ApiV1IpaddressesPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_platform_service_error_component import (
            ApiV1IpaddressesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_prefix_id_error_component import (
            ApiV1IpaddressesPartialUpdatePrefixIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_provider_error_component import (
            ApiV1IpaddressesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_provider_id_error_component import (
            ApiV1IpaddressesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_provider_reference_error_component import (
            ApiV1IpaddressesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_reconciliation_enabled_error_component import (
            ApiV1IpaddressesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_sla_availability_error_component import (
            ApiV1IpaddressesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_sla_target_error_component import (
            ApiV1IpaddressesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_slo_availability_error_component import (
            ApiV1IpaddressesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_slo_target_error_component import (
            ApiV1IpaddressesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_target_availability_error_component import (
            ApiV1IpaddressesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_tolerations_error_component import (
            ApiV1IpaddressesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_workspace_id_error_component import (
            ApiV1IpaddressesPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesPartialUpdatePrefixIdErrorComponent):
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
        from ..models.api_v1_ipaddresses_partial_update_annotations_error_component import (
            ApiV1IpaddressesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_archived_at_error_component import (
            ApiV1IpaddressesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_archived_error_component import (
            ApiV1IpaddressesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_archived_reason_error_component import (
            ApiV1IpaddressesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_credential_id_error_component import (
            ApiV1IpaddressesPartialUpdateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_criticality_error_component import (
            ApiV1IpaddressesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_debug_mode_error_component import (
            ApiV1IpaddressesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_display_name_error_component import (
            ApiV1IpaddressesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_ip_address_error_component import (
            ApiV1IpaddressesPartialUpdateIpAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_kind_error_component import (
            ApiV1IpaddressesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_labels_error_component import (
            ApiV1IpaddressesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_name_error_component import (
            ApiV1IpaddressesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_non_field_errors_error_component import (
            ApiV1IpaddressesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_organization_id_error_component import (
            ApiV1IpaddressesPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_platform_service_error_component import (
            ApiV1IpaddressesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_prefix_id_error_component import (
            ApiV1IpaddressesPartialUpdatePrefixIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_provider_error_component import (
            ApiV1IpaddressesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_provider_id_error_component import (
            ApiV1IpaddressesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_provider_reference_error_component import (
            ApiV1IpaddressesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_reconciliation_enabled_error_component import (
            ApiV1IpaddressesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_sla_availability_error_component import (
            ApiV1IpaddressesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_sla_target_error_component import (
            ApiV1IpaddressesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_slo_availability_error_component import (
            ApiV1IpaddressesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_slo_target_error_component import (
            ApiV1IpaddressesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_target_availability_error_component import (
            ApiV1IpaddressesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_tolerations_error_component import (
            ApiV1IpaddressesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_partial_update_workspace_id_error_component import (
            ApiV1IpaddressesPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1IpaddressesPartialUpdateAnnotationsErrorComponent
                | ApiV1IpaddressesPartialUpdateArchivedAtErrorComponent
                | ApiV1IpaddressesPartialUpdateArchivedErrorComponent
                | ApiV1IpaddressesPartialUpdateArchivedReasonErrorComponent
                | ApiV1IpaddressesPartialUpdateCredentialIdErrorComponent
                | ApiV1IpaddressesPartialUpdateCriticalityErrorComponent
                | ApiV1IpaddressesPartialUpdateDebugModeErrorComponent
                | ApiV1IpaddressesPartialUpdateDisplayNameErrorComponent
                | ApiV1IpaddressesPartialUpdateIpAddressErrorComponent
                | ApiV1IpaddressesPartialUpdateKindErrorComponent
                | ApiV1IpaddressesPartialUpdateLabelsErrorComponent
                | ApiV1IpaddressesPartialUpdateNameErrorComponent
                | ApiV1IpaddressesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1IpaddressesPartialUpdateOrganizationIdErrorComponent
                | ApiV1IpaddressesPartialUpdatePlatformServiceErrorComponent
                | ApiV1IpaddressesPartialUpdatePrefixIdErrorComponent
                | ApiV1IpaddressesPartialUpdateProviderErrorComponent
                | ApiV1IpaddressesPartialUpdateProviderIdErrorComponent
                | ApiV1IpaddressesPartialUpdateProviderReferenceErrorComponent
                | ApiV1IpaddressesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1IpaddressesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1IpaddressesPartialUpdateSlaTargetErrorComponent
                | ApiV1IpaddressesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1IpaddressesPartialUpdateSloTargetErrorComponent
                | ApiV1IpaddressesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1IpaddressesPartialUpdateTolerationsErrorComponent
                | ApiV1IpaddressesPartialUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_0 = (
                        ApiV1IpaddressesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_1 = (
                        ApiV1IpaddressesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_2 = (
                        ApiV1IpaddressesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_3 = (
                        ApiV1IpaddressesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_4 = (
                        ApiV1IpaddressesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_5 = (
                        ApiV1IpaddressesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_6 = (
                        ApiV1IpaddressesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_7 = (
                        ApiV1IpaddressesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_8 = (
                        ApiV1IpaddressesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_9 = (
                        ApiV1IpaddressesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_10 = (
                        ApiV1IpaddressesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_11 = (
                        ApiV1IpaddressesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_12 = (
                        ApiV1IpaddressesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_13 = (
                        ApiV1IpaddressesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_14 = (
                        ApiV1IpaddressesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_15 = (
                        ApiV1IpaddressesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_16 = (
                        ApiV1IpaddressesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_17 = (
                        ApiV1IpaddressesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_18 = (
                        ApiV1IpaddressesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_19 = (
                        ApiV1IpaddressesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_20 = (
                        ApiV1IpaddressesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_21 = (
                        ApiV1IpaddressesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_22 = (
                        ApiV1IpaddressesPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_23 = (
                        ApiV1IpaddressesPartialUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_24 = (
                        ApiV1IpaddressesPartialUpdateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_partial_update_error_type_25 = (
                        ApiV1IpaddressesPartialUpdatePrefixIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_ipaddresses_partial_update_error_type_26 = (
                    ApiV1IpaddressesPartialUpdateIpAddressErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_ipaddresses_partial_update_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_ipaddresses_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_ipaddresses_partial_update_validation_error.additional_properties = d
        return api_v1_ipaddresses_partial_update_validation_error

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
