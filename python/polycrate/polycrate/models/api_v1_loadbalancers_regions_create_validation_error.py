from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_loadbalancers_regions_create_active_error_component import (
        ApiV1LoadbalancersRegionsCreateActiveErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_annotations_error_component import (
        ApiV1LoadbalancersRegionsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_archived_at_error_component import (
        ApiV1LoadbalancersRegionsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_archived_error_component import (
        ApiV1LoadbalancersRegionsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_archived_reason_error_component import (
        ApiV1LoadbalancersRegionsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_criticality_error_component import (
        ApiV1LoadbalancersRegionsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_debug_mode_error_component import (
        ApiV1LoadbalancersRegionsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_description_error_component import (
        ApiV1LoadbalancersRegionsCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_display_name_error_component import (
        ApiV1LoadbalancersRegionsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_external_traffic_policy_error_component import (
        ApiV1LoadbalancersRegionsCreateExternalTrafficPolicyErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_kind_error_component import (
        ApiV1LoadbalancersRegionsCreateKindErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_labels_error_component import (
        ApiV1LoadbalancersRegionsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_name_error_component import (
        ApiV1LoadbalancersRegionsCreateNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_non_field_errors_error_component import (
        ApiV1LoadbalancersRegionsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_platform_service_error_component import (
        ApiV1LoadbalancersRegionsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_provider_error_component import (
        ApiV1LoadbalancersRegionsCreateProviderErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_provider_id_error_component import (
        ApiV1LoadbalancersRegionsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_provider_reference_error_component import (
        ApiV1LoadbalancersRegionsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_reconciliation_enabled_error_component import (
        ApiV1LoadbalancersRegionsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_region_config_error_component import (
        ApiV1LoadbalancersRegionsCreateRegionConfigErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_region_name_error_component import (
        ApiV1LoadbalancersRegionsCreateRegionNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_sla_availability_error_component import (
        ApiV1LoadbalancersRegionsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_sla_target_error_component import (
        ApiV1LoadbalancersRegionsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_slo_availability_error_component import (
        ApiV1LoadbalancersRegionsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_slo_target_error_component import (
        ApiV1LoadbalancersRegionsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_slug_error_component import (
        ApiV1LoadbalancersRegionsCreateSlugErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_create_target_availability_error_component import (
        ApiV1LoadbalancersRegionsCreateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1LoadbalancersRegionsCreateValidationError")


@_attrs_define
class ApiV1LoadbalancersRegionsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1LoadbalancersRegionsCreateActiveErrorComponent |
            ApiV1LoadbalancersRegionsCreateAnnotationsErrorComponent |
            ApiV1LoadbalancersRegionsCreateArchivedAtErrorComponent | ApiV1LoadbalancersRegionsCreateArchivedErrorComponent
            | ApiV1LoadbalancersRegionsCreateArchivedReasonErrorComponent |
            ApiV1LoadbalancersRegionsCreateCriticalityErrorComponent |
            ApiV1LoadbalancersRegionsCreateDebugModeErrorComponent |
            ApiV1LoadbalancersRegionsCreateDescriptionErrorComponent |
            ApiV1LoadbalancersRegionsCreateDisplayNameErrorComponent |
            ApiV1LoadbalancersRegionsCreateExternalTrafficPolicyErrorComponent |
            ApiV1LoadbalancersRegionsCreateKindErrorComponent | ApiV1LoadbalancersRegionsCreateLabelsErrorComponent |
            ApiV1LoadbalancersRegionsCreateNameErrorComponent | ApiV1LoadbalancersRegionsCreateNonFieldErrorsErrorComponent
            | ApiV1LoadbalancersRegionsCreatePlatformServiceErrorComponent |
            ApiV1LoadbalancersRegionsCreateProviderErrorComponent | ApiV1LoadbalancersRegionsCreateProviderIdErrorComponent
            | ApiV1LoadbalancersRegionsCreateProviderReferenceErrorComponent |
            ApiV1LoadbalancersRegionsCreateReconciliationEnabledErrorComponent |
            ApiV1LoadbalancersRegionsCreateRegionConfigErrorComponent |
            ApiV1LoadbalancersRegionsCreateRegionNameErrorComponent |
            ApiV1LoadbalancersRegionsCreateSlaAvailabilityErrorComponent |
            ApiV1LoadbalancersRegionsCreateSlaTargetErrorComponent |
            ApiV1LoadbalancersRegionsCreateSloAvailabilityErrorComponent |
            ApiV1LoadbalancersRegionsCreateSloTargetErrorComponent | ApiV1LoadbalancersRegionsCreateSlugErrorComponent |
            ApiV1LoadbalancersRegionsCreateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1LoadbalancersRegionsCreateActiveErrorComponent
        | ApiV1LoadbalancersRegionsCreateAnnotationsErrorComponent
        | ApiV1LoadbalancersRegionsCreateArchivedAtErrorComponent
        | ApiV1LoadbalancersRegionsCreateArchivedErrorComponent
        | ApiV1LoadbalancersRegionsCreateArchivedReasonErrorComponent
        | ApiV1LoadbalancersRegionsCreateCriticalityErrorComponent
        | ApiV1LoadbalancersRegionsCreateDebugModeErrorComponent
        | ApiV1LoadbalancersRegionsCreateDescriptionErrorComponent
        | ApiV1LoadbalancersRegionsCreateDisplayNameErrorComponent
        | ApiV1LoadbalancersRegionsCreateExternalTrafficPolicyErrorComponent
        | ApiV1LoadbalancersRegionsCreateKindErrorComponent
        | ApiV1LoadbalancersRegionsCreateLabelsErrorComponent
        | ApiV1LoadbalancersRegionsCreateNameErrorComponent
        | ApiV1LoadbalancersRegionsCreateNonFieldErrorsErrorComponent
        | ApiV1LoadbalancersRegionsCreatePlatformServiceErrorComponent
        | ApiV1LoadbalancersRegionsCreateProviderErrorComponent
        | ApiV1LoadbalancersRegionsCreateProviderIdErrorComponent
        | ApiV1LoadbalancersRegionsCreateProviderReferenceErrorComponent
        | ApiV1LoadbalancersRegionsCreateReconciliationEnabledErrorComponent
        | ApiV1LoadbalancersRegionsCreateRegionConfigErrorComponent
        | ApiV1LoadbalancersRegionsCreateRegionNameErrorComponent
        | ApiV1LoadbalancersRegionsCreateSlaAvailabilityErrorComponent
        | ApiV1LoadbalancersRegionsCreateSlaTargetErrorComponent
        | ApiV1LoadbalancersRegionsCreateSloAvailabilityErrorComponent
        | ApiV1LoadbalancersRegionsCreateSloTargetErrorComponent
        | ApiV1LoadbalancersRegionsCreateSlugErrorComponent
        | ApiV1LoadbalancersRegionsCreateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_loadbalancers_regions_create_active_error_component import (
            ApiV1LoadbalancersRegionsCreateActiveErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_annotations_error_component import (
            ApiV1LoadbalancersRegionsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_archived_at_error_component import (
            ApiV1LoadbalancersRegionsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_archived_error_component import (
            ApiV1LoadbalancersRegionsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_archived_reason_error_component import (
            ApiV1LoadbalancersRegionsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_criticality_error_component import (
            ApiV1LoadbalancersRegionsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_debug_mode_error_component import (
            ApiV1LoadbalancersRegionsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_description_error_component import (
            ApiV1LoadbalancersRegionsCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_display_name_error_component import (
            ApiV1LoadbalancersRegionsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_kind_error_component import (
            ApiV1LoadbalancersRegionsCreateKindErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_labels_error_component import (
            ApiV1LoadbalancersRegionsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_name_error_component import (
            ApiV1LoadbalancersRegionsCreateNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_non_field_errors_error_component import (
            ApiV1LoadbalancersRegionsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_platform_service_error_component import (
            ApiV1LoadbalancersRegionsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_provider_error_component import (
            ApiV1LoadbalancersRegionsCreateProviderErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_provider_id_error_component import (
            ApiV1LoadbalancersRegionsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_provider_reference_error_component import (
            ApiV1LoadbalancersRegionsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_reconciliation_enabled_error_component import (
            ApiV1LoadbalancersRegionsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_region_config_error_component import (
            ApiV1LoadbalancersRegionsCreateRegionConfigErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_region_name_error_component import (
            ApiV1LoadbalancersRegionsCreateRegionNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_sla_availability_error_component import (
            ApiV1LoadbalancersRegionsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_sla_target_error_component import (
            ApiV1LoadbalancersRegionsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_slo_availability_error_component import (
            ApiV1LoadbalancersRegionsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_slo_target_error_component import (
            ApiV1LoadbalancersRegionsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_slug_error_component import (
            ApiV1LoadbalancersRegionsCreateSlugErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_target_availability_error_component import (
            ApiV1LoadbalancersRegionsCreateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateRegionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsCreateRegionConfigErrorComponent):
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
        from ..models.api_v1_loadbalancers_regions_create_active_error_component import (
            ApiV1LoadbalancersRegionsCreateActiveErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_annotations_error_component import (
            ApiV1LoadbalancersRegionsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_archived_at_error_component import (
            ApiV1LoadbalancersRegionsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_archived_error_component import (
            ApiV1LoadbalancersRegionsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_archived_reason_error_component import (
            ApiV1LoadbalancersRegionsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_criticality_error_component import (
            ApiV1LoadbalancersRegionsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_debug_mode_error_component import (
            ApiV1LoadbalancersRegionsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_description_error_component import (
            ApiV1LoadbalancersRegionsCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_display_name_error_component import (
            ApiV1LoadbalancersRegionsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_external_traffic_policy_error_component import (
            ApiV1LoadbalancersRegionsCreateExternalTrafficPolicyErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_kind_error_component import (
            ApiV1LoadbalancersRegionsCreateKindErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_labels_error_component import (
            ApiV1LoadbalancersRegionsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_name_error_component import (
            ApiV1LoadbalancersRegionsCreateNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_non_field_errors_error_component import (
            ApiV1LoadbalancersRegionsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_platform_service_error_component import (
            ApiV1LoadbalancersRegionsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_provider_error_component import (
            ApiV1LoadbalancersRegionsCreateProviderErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_provider_id_error_component import (
            ApiV1LoadbalancersRegionsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_provider_reference_error_component import (
            ApiV1LoadbalancersRegionsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_reconciliation_enabled_error_component import (
            ApiV1LoadbalancersRegionsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_region_config_error_component import (
            ApiV1LoadbalancersRegionsCreateRegionConfigErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_region_name_error_component import (
            ApiV1LoadbalancersRegionsCreateRegionNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_sla_availability_error_component import (
            ApiV1LoadbalancersRegionsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_sla_target_error_component import (
            ApiV1LoadbalancersRegionsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_slo_availability_error_component import (
            ApiV1LoadbalancersRegionsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_slo_target_error_component import (
            ApiV1LoadbalancersRegionsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_slug_error_component import (
            ApiV1LoadbalancersRegionsCreateSlugErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_create_target_availability_error_component import (
            ApiV1LoadbalancersRegionsCreateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1LoadbalancersRegionsCreateActiveErrorComponent
                | ApiV1LoadbalancersRegionsCreateAnnotationsErrorComponent
                | ApiV1LoadbalancersRegionsCreateArchivedAtErrorComponent
                | ApiV1LoadbalancersRegionsCreateArchivedErrorComponent
                | ApiV1LoadbalancersRegionsCreateArchivedReasonErrorComponent
                | ApiV1LoadbalancersRegionsCreateCriticalityErrorComponent
                | ApiV1LoadbalancersRegionsCreateDebugModeErrorComponent
                | ApiV1LoadbalancersRegionsCreateDescriptionErrorComponent
                | ApiV1LoadbalancersRegionsCreateDisplayNameErrorComponent
                | ApiV1LoadbalancersRegionsCreateExternalTrafficPolicyErrorComponent
                | ApiV1LoadbalancersRegionsCreateKindErrorComponent
                | ApiV1LoadbalancersRegionsCreateLabelsErrorComponent
                | ApiV1LoadbalancersRegionsCreateNameErrorComponent
                | ApiV1LoadbalancersRegionsCreateNonFieldErrorsErrorComponent
                | ApiV1LoadbalancersRegionsCreatePlatformServiceErrorComponent
                | ApiV1LoadbalancersRegionsCreateProviderErrorComponent
                | ApiV1LoadbalancersRegionsCreateProviderIdErrorComponent
                | ApiV1LoadbalancersRegionsCreateProviderReferenceErrorComponent
                | ApiV1LoadbalancersRegionsCreateReconciliationEnabledErrorComponent
                | ApiV1LoadbalancersRegionsCreateRegionConfigErrorComponent
                | ApiV1LoadbalancersRegionsCreateRegionNameErrorComponent
                | ApiV1LoadbalancersRegionsCreateSlaAvailabilityErrorComponent
                | ApiV1LoadbalancersRegionsCreateSlaTargetErrorComponent
                | ApiV1LoadbalancersRegionsCreateSloAvailabilityErrorComponent
                | ApiV1LoadbalancersRegionsCreateSloTargetErrorComponent
                | ApiV1LoadbalancersRegionsCreateSlugErrorComponent
                | ApiV1LoadbalancersRegionsCreateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_0 = (
                        ApiV1LoadbalancersRegionsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_1 = (
                        ApiV1LoadbalancersRegionsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_2 = (
                        ApiV1LoadbalancersRegionsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_3 = (
                        ApiV1LoadbalancersRegionsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_4 = (
                        ApiV1LoadbalancersRegionsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_5 = (
                        ApiV1LoadbalancersRegionsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_6 = (
                        ApiV1LoadbalancersRegionsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_7 = (
                        ApiV1LoadbalancersRegionsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_8 = (
                        ApiV1LoadbalancersRegionsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_9 = (
                        ApiV1LoadbalancersRegionsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_10 = (
                        ApiV1LoadbalancersRegionsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_11 = (
                        ApiV1LoadbalancersRegionsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_12 = (
                        ApiV1LoadbalancersRegionsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_13 = (
                        ApiV1LoadbalancersRegionsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_14 = (
                        ApiV1LoadbalancersRegionsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_15 = (
                        ApiV1LoadbalancersRegionsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_16 = (
                        ApiV1LoadbalancersRegionsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_17 = (
                        ApiV1LoadbalancersRegionsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_18 = (
                        ApiV1LoadbalancersRegionsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_19 = (
                        ApiV1LoadbalancersRegionsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_20 = (
                        ApiV1LoadbalancersRegionsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_21 = (
                        ApiV1LoadbalancersRegionsCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_22 = (
                        ApiV1LoadbalancersRegionsCreateRegionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_23 = (
                        ApiV1LoadbalancersRegionsCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_24 = (
                        ApiV1LoadbalancersRegionsCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_create_error_type_25 = (
                        ApiV1LoadbalancersRegionsCreateRegionConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_loadbalancers_regions_create_error_type_26 = (
                    ApiV1LoadbalancersRegionsCreateExternalTrafficPolicyErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_loadbalancers_regions_create_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_loadbalancers_regions_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_loadbalancers_regions_create_validation_error.additional_properties = d
        return api_v1_loadbalancers_regions_create_validation_error

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
