from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_loadbalancers_regions_archive_create_active_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateActiveErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_annotations_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_archived_at_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_archived_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_archived_reason_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_criticality_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_debug_mode_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_description_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_display_name_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_external_traffic_policy_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateExternalTrafficPolicyErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_kind_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_labels_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_name_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_non_field_errors_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_platform_service_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_provider_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_provider_id_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_provider_reference_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_reconciliation_enabled_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_region_config_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateRegionConfigErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_region_name_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateRegionNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_sla_availability_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_sla_target_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_slo_availability_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_slo_target_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_slug_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateSlugErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_archive_create_target_availability_error_component import (
        ApiV1LoadbalancersRegionsArchiveCreateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1LoadbalancersRegionsArchiveCreateValidationError")


@_attrs_define
class ApiV1LoadbalancersRegionsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1LoadbalancersRegionsArchiveCreateActiveErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateAnnotationsErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateArchivedAtErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateArchivedErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateArchivedReasonErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateCriticalityErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateDebugModeErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateDescriptionErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateDisplayNameErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateExternalTrafficPolicyErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateKindErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateLabelsErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateNameErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreatePlatformServiceErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateProviderErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateProviderIdErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateProviderReferenceErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateRegionConfigErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateRegionNameErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateSlaTargetErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateSloTargetErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateSlugErrorComponent |
            ApiV1LoadbalancersRegionsArchiveCreateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1LoadbalancersRegionsArchiveCreateActiveErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateAnnotationsErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateArchivedAtErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateArchivedErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateArchivedReasonErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateCriticalityErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateDebugModeErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateDescriptionErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateDisplayNameErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateExternalTrafficPolicyErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateKindErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateLabelsErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateNameErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreatePlatformServiceErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateProviderErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateProviderIdErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateProviderReferenceErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateRegionConfigErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateRegionNameErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateSlaTargetErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateSloTargetErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateSlugErrorComponent
        | ApiV1LoadbalancersRegionsArchiveCreateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_loadbalancers_regions_archive_create_active_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateActiveErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_annotations_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_archived_at_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_archived_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_archived_reason_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_criticality_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_debug_mode_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_description_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_display_name_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_kind_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_labels_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_name_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_non_field_errors_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_platform_service_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_provider_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_provider_id_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_provider_reference_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_reconciliation_enabled_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_region_config_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateRegionConfigErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_region_name_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateRegionNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_sla_availability_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_sla_target_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_slo_availability_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_slo_target_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_slug_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateSlugErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_target_availability_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateRegionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsArchiveCreateRegionConfigErrorComponent):
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
        from ..models.api_v1_loadbalancers_regions_archive_create_active_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateActiveErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_annotations_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_archived_at_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_archived_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_archived_reason_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_criticality_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_debug_mode_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_description_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_display_name_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_external_traffic_policy_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateExternalTrafficPolicyErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_kind_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_labels_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_name_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_non_field_errors_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_platform_service_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_provider_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_provider_id_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_provider_reference_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_reconciliation_enabled_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_region_config_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateRegionConfigErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_region_name_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateRegionNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_sla_availability_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_sla_target_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_slo_availability_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_slo_target_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_slug_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateSlugErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_archive_create_target_availability_error_component import (
            ApiV1LoadbalancersRegionsArchiveCreateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1LoadbalancersRegionsArchiveCreateActiveErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateAnnotationsErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateArchivedAtErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateArchivedErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateArchivedReasonErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateCriticalityErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateDebugModeErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateDescriptionErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateDisplayNameErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateExternalTrafficPolicyErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateKindErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateLabelsErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateNameErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreatePlatformServiceErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateProviderErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateProviderIdErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateProviderReferenceErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateRegionConfigErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateRegionNameErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateSlaTargetErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateSloTargetErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateSlugErrorComponent
                | ApiV1LoadbalancersRegionsArchiveCreateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_0 = (
                        ApiV1LoadbalancersRegionsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_1 = (
                        ApiV1LoadbalancersRegionsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_2 = (
                        ApiV1LoadbalancersRegionsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_3 = (
                        ApiV1LoadbalancersRegionsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_4 = (
                        ApiV1LoadbalancersRegionsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_5 = (
                        ApiV1LoadbalancersRegionsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_6 = (
                        ApiV1LoadbalancersRegionsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_7 = (
                        ApiV1LoadbalancersRegionsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_8 = (
                        ApiV1LoadbalancersRegionsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_9 = (
                        ApiV1LoadbalancersRegionsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_10 = (
                        ApiV1LoadbalancersRegionsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_11 = (
                        ApiV1LoadbalancersRegionsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_12 = (
                        ApiV1LoadbalancersRegionsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_13 = (
                        ApiV1LoadbalancersRegionsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_14 = (
                        ApiV1LoadbalancersRegionsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_15 = (
                        ApiV1LoadbalancersRegionsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_16 = (
                        ApiV1LoadbalancersRegionsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_17 = (
                        ApiV1LoadbalancersRegionsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_18 = (
                        ApiV1LoadbalancersRegionsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_19 = (
                        ApiV1LoadbalancersRegionsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_20 = (
                        ApiV1LoadbalancersRegionsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_21 = (
                        ApiV1LoadbalancersRegionsArchiveCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_22 = (
                        ApiV1LoadbalancersRegionsArchiveCreateRegionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_23 = (
                        ApiV1LoadbalancersRegionsArchiveCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_24 = (
                        ApiV1LoadbalancersRegionsArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_25 = (
                        ApiV1LoadbalancersRegionsArchiveCreateRegionConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_26 = (
                    ApiV1LoadbalancersRegionsArchiveCreateExternalTrafficPolicyErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_loadbalancers_regions_archive_create_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_loadbalancers_regions_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_loadbalancers_regions_archive_create_validation_error.additional_properties = d
        return api_v1_loadbalancers_regions_archive_create_validation_error

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
