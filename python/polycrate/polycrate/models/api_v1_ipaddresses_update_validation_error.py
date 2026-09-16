from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_ipaddresses_update_annotations_error_component import (
        ApiV1IpaddressesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_archived_at_error_component import (
        ApiV1IpaddressesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_archived_error_component import ApiV1IpaddressesUpdateArchivedErrorComponent
    from ..models.api_v1_ipaddresses_update_archived_reason_error_component import (
        ApiV1IpaddressesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_credential_id_error_component import (
        ApiV1IpaddressesUpdateCredentialIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_criticality_error_component import (
        ApiV1IpaddressesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_debug_mode_error_component import (
        ApiV1IpaddressesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_display_name_error_component import (
        ApiV1IpaddressesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_ip_address_error_component import (
        ApiV1IpaddressesUpdateIpAddressErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_kind_error_component import ApiV1IpaddressesUpdateKindErrorComponent
    from ..models.api_v1_ipaddresses_update_labels_error_component import ApiV1IpaddressesUpdateLabelsErrorComponent
    from ..models.api_v1_ipaddresses_update_name_error_component import ApiV1IpaddressesUpdateNameErrorComponent
    from ..models.api_v1_ipaddresses_update_non_field_errors_error_component import (
        ApiV1IpaddressesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_organization_id_error_component import (
        ApiV1IpaddressesUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_platform_service_error_component import (
        ApiV1IpaddressesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_prefix_id_error_component import (
        ApiV1IpaddressesUpdatePrefixIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_provider_error_component import ApiV1IpaddressesUpdateProviderErrorComponent
    from ..models.api_v1_ipaddresses_update_provider_id_error_component import (
        ApiV1IpaddressesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_provider_reference_error_component import (
        ApiV1IpaddressesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_reconciliation_enabled_error_component import (
        ApiV1IpaddressesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_sla_availability_error_component import (
        ApiV1IpaddressesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_sla_target_error_component import (
        ApiV1IpaddressesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_slo_availability_error_component import (
        ApiV1IpaddressesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_slo_target_error_component import (
        ApiV1IpaddressesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_target_availability_error_component import (
        ApiV1IpaddressesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_tolerations_error_component import (
        ApiV1IpaddressesUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_ipaddresses_update_workspace_id_error_component import (
        ApiV1IpaddressesUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1IpaddressesUpdateValidationError")


@_attrs_define
class ApiV1IpaddressesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1IpaddressesUpdateAnnotationsErrorComponent | ApiV1IpaddressesUpdateArchivedAtErrorComponent |
            ApiV1IpaddressesUpdateArchivedErrorComponent | ApiV1IpaddressesUpdateArchivedReasonErrorComponent |
            ApiV1IpaddressesUpdateCredentialIdErrorComponent | ApiV1IpaddressesUpdateCriticalityErrorComponent |
            ApiV1IpaddressesUpdateDebugModeErrorComponent | ApiV1IpaddressesUpdateDisplayNameErrorComponent |
            ApiV1IpaddressesUpdateIpAddressErrorComponent | ApiV1IpaddressesUpdateKindErrorComponent |
            ApiV1IpaddressesUpdateLabelsErrorComponent | ApiV1IpaddressesUpdateNameErrorComponent |
            ApiV1IpaddressesUpdateNonFieldErrorsErrorComponent | ApiV1IpaddressesUpdateOrganizationIdErrorComponent |
            ApiV1IpaddressesUpdatePlatformServiceErrorComponent | ApiV1IpaddressesUpdatePrefixIdErrorComponent |
            ApiV1IpaddressesUpdateProviderErrorComponent | ApiV1IpaddressesUpdateProviderIdErrorComponent |
            ApiV1IpaddressesUpdateProviderReferenceErrorComponent |
            ApiV1IpaddressesUpdateReconciliationEnabledErrorComponent | ApiV1IpaddressesUpdateSlaAvailabilityErrorComponent
            | ApiV1IpaddressesUpdateSlaTargetErrorComponent | ApiV1IpaddressesUpdateSloAvailabilityErrorComponent |
            ApiV1IpaddressesUpdateSloTargetErrorComponent | ApiV1IpaddressesUpdateTargetAvailabilityErrorComponent |
            ApiV1IpaddressesUpdateTolerationsErrorComponent | ApiV1IpaddressesUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1IpaddressesUpdateAnnotationsErrorComponent
        | ApiV1IpaddressesUpdateArchivedAtErrorComponent
        | ApiV1IpaddressesUpdateArchivedErrorComponent
        | ApiV1IpaddressesUpdateArchivedReasonErrorComponent
        | ApiV1IpaddressesUpdateCredentialIdErrorComponent
        | ApiV1IpaddressesUpdateCriticalityErrorComponent
        | ApiV1IpaddressesUpdateDebugModeErrorComponent
        | ApiV1IpaddressesUpdateDisplayNameErrorComponent
        | ApiV1IpaddressesUpdateIpAddressErrorComponent
        | ApiV1IpaddressesUpdateKindErrorComponent
        | ApiV1IpaddressesUpdateLabelsErrorComponent
        | ApiV1IpaddressesUpdateNameErrorComponent
        | ApiV1IpaddressesUpdateNonFieldErrorsErrorComponent
        | ApiV1IpaddressesUpdateOrganizationIdErrorComponent
        | ApiV1IpaddressesUpdatePlatformServiceErrorComponent
        | ApiV1IpaddressesUpdatePrefixIdErrorComponent
        | ApiV1IpaddressesUpdateProviderErrorComponent
        | ApiV1IpaddressesUpdateProviderIdErrorComponent
        | ApiV1IpaddressesUpdateProviderReferenceErrorComponent
        | ApiV1IpaddressesUpdateReconciliationEnabledErrorComponent
        | ApiV1IpaddressesUpdateSlaAvailabilityErrorComponent
        | ApiV1IpaddressesUpdateSlaTargetErrorComponent
        | ApiV1IpaddressesUpdateSloAvailabilityErrorComponent
        | ApiV1IpaddressesUpdateSloTargetErrorComponent
        | ApiV1IpaddressesUpdateTargetAvailabilityErrorComponent
        | ApiV1IpaddressesUpdateTolerationsErrorComponent
        | ApiV1IpaddressesUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_ipaddresses_update_annotations_error_component import (
            ApiV1IpaddressesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_archived_at_error_component import (
            ApiV1IpaddressesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_archived_error_component import (
            ApiV1IpaddressesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_archived_reason_error_component import (
            ApiV1IpaddressesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_credential_id_error_component import (
            ApiV1IpaddressesUpdateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_criticality_error_component import (
            ApiV1IpaddressesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_debug_mode_error_component import (
            ApiV1IpaddressesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_display_name_error_component import (
            ApiV1IpaddressesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_kind_error_component import (
            ApiV1IpaddressesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_labels_error_component import (
            ApiV1IpaddressesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_name_error_component import (
            ApiV1IpaddressesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_non_field_errors_error_component import (
            ApiV1IpaddressesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_organization_id_error_component import (
            ApiV1IpaddressesUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_platform_service_error_component import (
            ApiV1IpaddressesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_prefix_id_error_component import (
            ApiV1IpaddressesUpdatePrefixIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_provider_error_component import (
            ApiV1IpaddressesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_provider_id_error_component import (
            ApiV1IpaddressesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_provider_reference_error_component import (
            ApiV1IpaddressesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_reconciliation_enabled_error_component import (
            ApiV1IpaddressesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_sla_availability_error_component import (
            ApiV1IpaddressesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_sla_target_error_component import (
            ApiV1IpaddressesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_slo_availability_error_component import (
            ApiV1IpaddressesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_slo_target_error_component import (
            ApiV1IpaddressesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_target_availability_error_component import (
            ApiV1IpaddressesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_tolerations_error_component import (
            ApiV1IpaddressesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_workspace_id_error_component import (
            ApiV1IpaddressesUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1IpaddressesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IpaddressesUpdatePrefixIdErrorComponent):
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
        from ..models.api_v1_ipaddresses_update_annotations_error_component import (
            ApiV1IpaddressesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_archived_at_error_component import (
            ApiV1IpaddressesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_archived_error_component import (
            ApiV1IpaddressesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_archived_reason_error_component import (
            ApiV1IpaddressesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_credential_id_error_component import (
            ApiV1IpaddressesUpdateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_criticality_error_component import (
            ApiV1IpaddressesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_debug_mode_error_component import (
            ApiV1IpaddressesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_display_name_error_component import (
            ApiV1IpaddressesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_ip_address_error_component import (
            ApiV1IpaddressesUpdateIpAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_kind_error_component import (
            ApiV1IpaddressesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_labels_error_component import (
            ApiV1IpaddressesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_name_error_component import (
            ApiV1IpaddressesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_non_field_errors_error_component import (
            ApiV1IpaddressesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_organization_id_error_component import (
            ApiV1IpaddressesUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_platform_service_error_component import (
            ApiV1IpaddressesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_prefix_id_error_component import (
            ApiV1IpaddressesUpdatePrefixIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_provider_error_component import (
            ApiV1IpaddressesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_provider_id_error_component import (
            ApiV1IpaddressesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_provider_reference_error_component import (
            ApiV1IpaddressesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_reconciliation_enabled_error_component import (
            ApiV1IpaddressesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_sla_availability_error_component import (
            ApiV1IpaddressesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_sla_target_error_component import (
            ApiV1IpaddressesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_slo_availability_error_component import (
            ApiV1IpaddressesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_slo_target_error_component import (
            ApiV1IpaddressesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_target_availability_error_component import (
            ApiV1IpaddressesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_tolerations_error_component import (
            ApiV1IpaddressesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_ipaddresses_update_workspace_id_error_component import (
            ApiV1IpaddressesUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1IpaddressesUpdateAnnotationsErrorComponent
                | ApiV1IpaddressesUpdateArchivedAtErrorComponent
                | ApiV1IpaddressesUpdateArchivedErrorComponent
                | ApiV1IpaddressesUpdateArchivedReasonErrorComponent
                | ApiV1IpaddressesUpdateCredentialIdErrorComponent
                | ApiV1IpaddressesUpdateCriticalityErrorComponent
                | ApiV1IpaddressesUpdateDebugModeErrorComponent
                | ApiV1IpaddressesUpdateDisplayNameErrorComponent
                | ApiV1IpaddressesUpdateIpAddressErrorComponent
                | ApiV1IpaddressesUpdateKindErrorComponent
                | ApiV1IpaddressesUpdateLabelsErrorComponent
                | ApiV1IpaddressesUpdateNameErrorComponent
                | ApiV1IpaddressesUpdateNonFieldErrorsErrorComponent
                | ApiV1IpaddressesUpdateOrganizationIdErrorComponent
                | ApiV1IpaddressesUpdatePlatformServiceErrorComponent
                | ApiV1IpaddressesUpdatePrefixIdErrorComponent
                | ApiV1IpaddressesUpdateProviderErrorComponent
                | ApiV1IpaddressesUpdateProviderIdErrorComponent
                | ApiV1IpaddressesUpdateProviderReferenceErrorComponent
                | ApiV1IpaddressesUpdateReconciliationEnabledErrorComponent
                | ApiV1IpaddressesUpdateSlaAvailabilityErrorComponent
                | ApiV1IpaddressesUpdateSlaTargetErrorComponent
                | ApiV1IpaddressesUpdateSloAvailabilityErrorComponent
                | ApiV1IpaddressesUpdateSloTargetErrorComponent
                | ApiV1IpaddressesUpdateTargetAvailabilityErrorComponent
                | ApiV1IpaddressesUpdateTolerationsErrorComponent
                | ApiV1IpaddressesUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_0 = (
                        ApiV1IpaddressesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_1 = (
                        ApiV1IpaddressesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_2 = (
                        ApiV1IpaddressesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_3 = (
                        ApiV1IpaddressesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_4 = (
                        ApiV1IpaddressesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_5 = (
                        ApiV1IpaddressesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_6 = (
                        ApiV1IpaddressesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_7 = (
                        ApiV1IpaddressesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_8 = (
                        ApiV1IpaddressesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_9 = (
                        ApiV1IpaddressesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_10 = (
                        ApiV1IpaddressesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_11 = (
                        ApiV1IpaddressesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_12 = (
                        ApiV1IpaddressesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_13 = (
                        ApiV1IpaddressesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_14 = (
                        ApiV1IpaddressesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_15 = (
                        ApiV1IpaddressesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_16 = (
                        ApiV1IpaddressesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_17 = (
                        ApiV1IpaddressesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_18 = (
                        ApiV1IpaddressesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_19 = (
                        ApiV1IpaddressesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_20 = (
                        ApiV1IpaddressesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_21 = (
                        ApiV1IpaddressesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_22 = (
                        ApiV1IpaddressesUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_23 = (
                        ApiV1IpaddressesUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_24 = (
                        ApiV1IpaddressesUpdateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_ipaddresses_update_error_type_25 = (
                        ApiV1IpaddressesUpdatePrefixIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_ipaddresses_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_ipaddresses_update_error_type_26 = (
                    ApiV1IpaddressesUpdateIpAddressErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_ipaddresses_update_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_ipaddresses_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_ipaddresses_update_validation_error.additional_properties = d
        return api_v1_ipaddresses_update_validation_error

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
